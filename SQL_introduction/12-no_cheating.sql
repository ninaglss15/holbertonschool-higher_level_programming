-- This command updates the score of a specific row in 'second_table'
-- Only the row where the 'name' column is equal to 'Bob' will be updated
-- SET assigns the new value (10) to the 'score' column
-- The WHERE clause ensures that only Bob's record is modified
UPDATE second_table
SET score = 10
WHERE name = 'Bob';