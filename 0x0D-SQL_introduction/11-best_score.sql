-- Description: Lists all records with a score greater than or equal to 10 in the table second_table from the database hbtn_0c_0, ordered by score (top first).
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
