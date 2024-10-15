import psycopg2
from config import TIMESCALE_DB

CONNECTION = TIMESCALE_DB

CREATE_EXTENSION = "CREATE EXTENSION IF NOT EXISTS vector"

CREATE_PODCAST_TABLE = """
CREATE TABLE IF NOT EXISTS podcast (
    id VARCHAR(255) PRIMARY KEY,
    title TEXT NOT NULL
);
"""
CREATE_SEGMENT_TABLE = """
CREATE TABLE IF NOT EXISTS podcast_segment (
    id VARCHAR(255) PRIMARY KEY,
    start_time FLOAT8 NOT NULL,
    end_time FLOAT8 NOT NULL,
    content TEXT NOT NULL,
    embedding vector(128) NOT NULL,
    podcast_id VARCHAR(255),
    FOREIGN KEY (podcast_id) REFERENCES podcast(id)
);
"""


def main():
    conn = psycopg2.connect(CONNECTION)
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute(CREATE_EXTENSION)
    cursor.execute(CREATE_PODCAST_TABLE)
    cursor.execute(CREATE_SEGMENT_TABLE)
    conn.commit()


if __name__ == '__main__':
    main()
