-- This command selects the 'score' and 'name' columns from 'second_table'
-- Only rows where the score is greater than or equal to 10 are included
-- The results are ordered by 'score' in descending order (highest first)
-- This script only displays data and does not modify the table
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;