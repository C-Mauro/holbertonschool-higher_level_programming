-- list the numbers of records with the same score
-- sorted descending
SELECT
    score COUNT(*) AS number
FROM
    second_table
GROUP BY
    score
ORDER BY
    score DESC;
