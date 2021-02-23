import re
import psycopg2
import pdb
from bible_book_regex import nt_regex


def verses_to_db(db_connection, path_to_file, regex_dict, bible_version):
    with open(path_to_file, 'r') as text:
        # pdb.set_trace()
        for line in text:
            line = line.strip()
            db_verse_insert(regex_dict, line, bible_version)


def db_verse_insert(regex_dict, verse_data, bible_version):
    sql_insert = """INSERT INTO new_testament(book, chapter, verse, {}) 
                    VALUES ({}, {}, {}, {})
                    ON CONFLICT (book, chapter, verse) DO 
                    UPDATE SET {} = {};"""
    cursor = conn.cursor()
    for book_name, regex in regex_dict.items():
        if re.match(regex, verse_data):
            match = re.search(regex, verse_data)
            verse_text = match.group(4).strip().replace("'", "''")

            version_col = bible_version
            book = repr(book_name)
            chapter = repr(match.group(2))
            verse = repr(match.group(3))
            verse_for_sql = f"'{verse_text} '"

            sql = sql_insert.format(
                bible_version,
                book, 
                chapter, 
                verse, 
                verse_for_sql,
                bible_version,
                verse_for_sql
            )
            cursor.execute(sql)


def create_table(db_connection):
    cursor = conn.cursor()
    cursor.execute(open('create_nt_table.sql', 'r').read())


if __name__ == '__main__':
    rcv_txt = 'rcv.txt'
    gk_txt = './nestle1904/nestle1904.txt'

    conn = psycopg2.connect(
        host='localhost',
        database='na28_rcv',
        user='postgres',
        password=''
    )
    conn.set_session(autocommit=True)

    create_table(conn)
    verses_to_db(conn, rcv_txt, nt_regex, 'recovery_version')
    verses_to_db(conn, gk_txt, nt_regex, 'nestle1904')