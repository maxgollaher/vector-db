import psycopg2
from config import TIMESCALE_DB
import tabulate as tb

CONNECTION = TIMESCALE_DB

conn = psycopg2.connect(CONNECTION)
cursor = conn.cursor()


def write_to_md(file_name: str, content: str):
    with open(file_name, 'a') as f:
        f.write(content)


def execute_question(query_func, question_number: str | int, headers: list[str], segment_id=None,
                     podcast_id=None, ascending=True, limit=5):
    input_text = get_segment(segment_id) if segment_id else get_podcast(podcast_id)
    item_id = segment_id if segment_id else podcast_id
    result, query = query_func(item_id, limit, ascending)
    result = [(r[0].replace('|', '\\|'), *r[1:]) for r in result]
    md_content = f"## Question {question_number} Query:\n\n```sql\n{query}\n```\n"
    md_content += f"### Question {question_number} Results:\n"
    md_content += f"**Input:** {input_text}\n\n"
    md_content += tb.tabulate(result, headers=headers, tablefmt='github') + "\n\n"
    md_content += '<div style="page-break-after: always;"></div>\n\n'
    write_to_md("results.md", md_content)


def get_segment(segment_id):
    cursor.execute(f"""
        SELECT 
            ps.content
        FROM podcast_segment ps
        JOIN podcast p ON ps.podcast_id = p.id
        WHERE ps.id = '{segment_id}';
    """)
    result = cursor.fetchall()
    return result[0][0]


def get_podcast(podcast_id):
    cursor.execute(f"""
        SELECT 
            p.title
        FROM podcast p
        WHERE p.id = '{podcast_id}';
    """)
    result = cursor.fetchall()
    return result[0][0]


def single_segment_similarity(segment_id: str, limit: int, ascending=True):
    query = f"""
SELECT 
    p.title,
    ps.id,
    ps.content,
    ps.start_time,
    ps.end_time,
    ps.embedding <-> (SELECT embedding FROM podcast_segment WHERE id = '{segment_id}' LIMIT 1) AS distance
FROM podcast_segment ps
JOIN podcast p ON ps.podcast_id = p.id
WHERE ps.id != '{segment_id}'
ORDER BY distance {'ASC' if ascending else 'DESC'}
LIMIT {limit};
"""
    cursor.execute(query)
    results = cursor.fetchall()
    return results, query


def single_segment_episode_similarity(segment_id: str, limit: int, ascending=True):
    query = f"""
SELECT 
    p.title,
    AVG(ps.embedding) <-> 
    (SELECT embedding FROM podcast_segment WHERE id = '{segment_id}' LIMIT 1) AS distance
FROM podcast_segment ps
JOIN podcast p ON ps.podcast_id = p.id
WHERE p.id != (SELECT podcast_id FROM podcast_segment WHERE id = '{segment_id}' LIMIT 1)
GROUP BY p.id, p.title
ORDER BY distance {'ASC' if ascending else 'DESC'}
LIMIT {limit};
"""
    cursor.execute(query)
    results = cursor.fetchall()
    return results, query


def single_podcast_similarity(podcast_id: str, limit: int, ascending=True):
    query = f"""
SELECT
    p.title,
    AVG(ps.embedding) <-> (
        SELECT AVG(embedding)
        FROM podcast_segment
        WHERE podcast_id = '{podcast_id}'
        LIMIT 1
    ) AS distance
FROM podcast_segment ps
JOIN podcast p ON ps.podcast_id = p.id
WHERE p.id != '{podcast_id}'
GROUP BY p.id, p.title
ORDER BY distance {'ASC' if ascending else 'DESC'}
LIMIT {limit};
"""
    cursor.execute(query)
    results = cursor.fetchall()
    return results, query


if __name__ == '__main__':
    with open("results.md", 'w') as f:
        f.write("# Podcast Similarity Results\n\n")

    headers = ['Podcast Title', 'Segment ID', 'Content', 'Start Time', 'End Time', 'Distance']
    execute_question(single_segment_similarity, 1, headers, '267:476')
    execute_question(single_segment_similarity, 2, headers, '267:476', ascending=False)
    execute_question(single_segment_similarity, 3, headers, '48:511')
    execute_question(single_segment_similarity, 4, headers, '51:56')

    headers = ['Podcast Title', 'Average Distance']
    execute_question(single_segment_episode_similarity, '5a', headers, '267:476')
    execute_question(single_segment_episode_similarity, '5b', headers, '48:511')
    execute_question(single_segment_episode_similarity, '5c', headers, '51:56')

    execute_question(single_podcast_similarity, 6, headers, podcast_id='VeH7qKZr0WI')
