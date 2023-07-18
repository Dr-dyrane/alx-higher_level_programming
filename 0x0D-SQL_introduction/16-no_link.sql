-- Description: Lists all records from the table second_table of the database hbtn_0c_0 in descending order of score, excluding rows without a name value. Results display the score and the name.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
