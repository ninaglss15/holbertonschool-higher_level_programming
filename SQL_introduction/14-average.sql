-- This command computes the average of all scores in the 'second_table'
-- AVG(score) calculates the mean value of the 'score' column
-- AS average gives a name to the resulting column so it will display as 'average'
-- FROM second_table specifies the table from which the scores are retrieved
SELECT AVG(score)
AS average
FROM second_table;