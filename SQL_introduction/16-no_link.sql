-- This command selects the 'score' and 'name' columns from 'second_table'
-- Only rows where 'name' has a value (not NULL and not an empty string) are included
-- The WHERE clause filters out rows where 'name' is NULL or ''
-- ORDER BY score DESC sorts the results so that the highest scores appear first
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;