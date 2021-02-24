SELECT column_name
FROM information_schema.columns
WHERE table_name = 'new_testament' 
    AND columns.data_type = 'text';