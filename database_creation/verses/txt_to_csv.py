import csv
import re
from bible_book_regex import nt_regex


def txt_to_csv(file_path, new_path):
    txt_file = open(file_path, "r")
    csv_file = open(new_path, "w")
    writer = csv.writer(csv_file, delimiter='|')
    for line in txt_file:
        line = line.strip()
        parsed_data = parse_for_csv(nt_regex, line)
        writer.writerow(parsed_data)


def parse_for_csv(regex_dict, verse_data):
    for book_name, regex in regex_dict.items():
        if re.match(regex, verse_data):
            match = re.search(regex, verse_data)

            # version_col = bible_version
            book = book_name
            chapter = match.group(2)
            if chapter == "":
                chapter = "1"
            verse = match.group(3)
            verse_text = match.group(4).replace("'", "''")

    return [book, chapter, verse, verse_text]


if __name__ == "__main__":
    # file_path = "./recovery_version/rcv.txt"
    # new_path = "./recovery_version/rcv.csv"
    file_path = "./nestle1904/nestle1904.txt"
    new_path = "./nestle1904/nestle1904.csv"

    txt_to_csv(file_path, new_path)
