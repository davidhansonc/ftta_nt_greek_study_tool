-- DROP TABLE IF EXISTS new_testament;

CREATE TABLE IF NOT EXISTS new_testament (
    verse_id SERIAL NOT NULL,
    book varchar(25) NOT NULL,
    chapter INT NOT NULL,
    verse INT NOT NULL,
    recovery_version text,
    nestle_aland28 text,
    nestle1904 text,
    amplified text,
    PRIMARY KEY (book, chapter, verse)
)