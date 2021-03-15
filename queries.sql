SELECT column_name
FROM information_schema.columns
WHERE table_name = 'new_testament' 
    AND columns.data_type = 'text';

\copy bible_books(book,chapter,verse,recovery_version,nestle1904) FROM '/Users/davidhansonc/Desktop/ftta_nt_greek_study_tool/combined_verse_table.csv' DELIMITER '|' CSV HEADER

\copy new_testament(book,chapter,verse,recovery_version,nestle1904) FROM '/Users/davidhansonc/Desktop/ftta_nt_greek_study_tool/combined_verse_table.csv' DELIMITER '|' CSV HEADER