DROP TABLE IF EXISTS nt_vocab;

CREATE TABLE nt_vocab (
    id SERIAL PRIMARY KEY NOT NULL,
    word varchar(25) NOT NULL,
    definition_gloss TEXT NOT NULL,
    frequency_rank INT NOT NULL,
    frequency_in_gnt INT NOT NULL,
    percent_of_gnt REAL NOT NULL
)