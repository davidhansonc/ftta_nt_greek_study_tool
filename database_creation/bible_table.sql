CREATE TABLE IF NOT EXISTS new_testament (
    verse_id SERIAL NOT NULL,
    book varchar(25) NOT NULL,
    chapter INT NOT NULL,
    verse INT NOT NULL,
    outline varchar(250),
    cross_reference INT [],
    footnote TEXT [],
    rcv text,
    na28 text,
    PRIMARY KEY (book, chapter, verse)
)