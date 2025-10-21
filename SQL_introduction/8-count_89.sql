-- This command counts the number of rows in the 'first_table' table
-- that have 'id' equal to 89
-- COUNT(*) is an aggregation function that counts all rows matching the condition
-- AS allows you to give a name (alias) to the resulting column
-- WHERE filters the rows to include only those that meet the specified condition
SELECT COUNT(*) AS first_table
FROM first_table
WHERE id = 89;