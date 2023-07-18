-- Description: Lists the number of records with the same score in the table second_table of the database hbtn_0c_0, sorted by the number of records in descending order.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
