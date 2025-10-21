-- This command lists each score in 'second_table' along with the number of records having that score
-- COUNT(*) counts all rows for each score
-- AS number renames the result column to 'number'
-- GROUP BY score groups all rows that have the same score
-- ORDER BY number DESC sorts the results so that scores with the most records appear first
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;