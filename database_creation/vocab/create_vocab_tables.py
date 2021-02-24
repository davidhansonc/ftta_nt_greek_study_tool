import csv
import psycopg2


def get_vocab(db_conn, db_cursor, file):
    with open(file, newline="") as vocab:
        csv_reader = csv.reader(vocab, delimiter=",", quotechar='"')
        for row in csv_reader:
            row = (A )  # get this to strip each entry
            db_insert(db_conn, db_cursor, tuple(row))


def db_insert(db_conn, db_cursor, csv_row):
    sql_insert = f"""INSERT INTO nt_vocab(id, word, definition_gloss, frequency_rank, 
            frequency_in_gnt, percent_of_gnt) VALUES {csv_row};"""
    db_cursor.execute(sql_insert)


def create_table(db_conn, db_cursor):
    db_cursor.execute(open("./create_vocab_table.sql", "r").read())


if __name__ == "__main__":
    vocab_info = "gnt_vocab.csv"

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="na28_rcv",
            user="davidhansonc",
            password=""
        )
        conn.set_session(autocommit=True)
        cursor = conn.cursor()

        create_table(conn, cursor)
        print("vocab table created")
        get_vocab(conn, cursor, vocab_info)

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL: ", error)
    
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
