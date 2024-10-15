import psycopg2
from config import TIMESCALE_DB

CONNECTION = TIMESCALE_DB

def main():
    drop_table = "DROP TABLE podcast, podcast_segment"

    with psycopg2.connect(CONNECTION) as conn:
        cursor = conn.cursor()
        cursor.execute(drop_table)

        conn.commit()
        cursor.close()


if __name__ == '__main__':
    main()
