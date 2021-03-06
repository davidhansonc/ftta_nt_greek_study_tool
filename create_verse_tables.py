import re
import psycopg2
from database_creation.verses.bible_book_regex import nt_regex


def verses_to_db(db_connection, db_cursor, path_to_file, regex_dict, bible_version):
    with open(path_to_file, "r") as text:
        # pdb.set_trace()
        for line in text:
            line = line.strip()
            db_verse_insert(db_cursor, regex_dict, line, bible_version)


def db_verse_insert(db_cursor, regex_dict, verse_data, bible_version):
    sql_insert = """INSERT INTO new_testament(book, chapter, verse, {}) 
                    VALUES ({}, {}, {}, {})
                    ON CONFLICT (book, chapter, verse) DO 
                    UPDATE SET {} = {};"""
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
            db_cursor.execute(sql)


def create_table(db_connection, db_cursor):
    db_cursor.execute(open("./database_creation/verses/create_nt_table.sql", "r").read())


def init_database():
    rcv_txt = "./database_creation/verses/recovery_version/rcv.txt"
    gk_txt = "./database_creation/verses/nestle1904/nestle1904.txt"

    try:
        # host = "ec2-50-16-108-41.compute-1.amazonaws.com"
        # database = "d923lfcqpkom3m"
        # user = "gchapifzwomimb"
        # password = "5be1227606be09cdc5fc4cb50bcafff0d1d32ea8572c6a2a10912d5481f7e3c5"
        host = "localhost"
        database = "na28_rcv"
        user = "davidhansonc"
        password = ""
        port = 5432
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        conn.set_session(autocommit=True)
        cursor = conn.cursor()

        create_table(conn, cursor)
        print("verse table created")
        verses_to_db(conn, cursor, rcv_txt, nt_regex, "recovery_version")
        print("Recovery Version verses filled")
        verses_to_db(conn, cursor, gk_txt, nt_regex, "nestle1904")
        print("Nestle Aland verses filled")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL: ", error)
    
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")


if __name__ == "__main__":
    init_database()