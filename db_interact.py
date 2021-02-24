import psycopg2
from sys import argv

try:
    conn = psycopg2.connect(
        host='localhost',
        database='na28_rcv',
        user='davidhansonc',
        password=''
    )
    cursor = conn.cursor()

    verse_reference = argv[1:4]
    bible_version = argv[4:]
    select_query = f"SELECT {bible_version[0]}, {bible_version[1]} FROM new_testament WHERE book={repr(verse_reference[0])} and chapter={repr(verse_reference[1])} and verse={repr(verse_reference[2])};"

    cursor.execute(select_query)
    verse_selection = cursor.fetchall()
    print(verse_selection[0][0])
    print(verse_selection[0][1])

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL: ", error)

finally:
    if conn:
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")