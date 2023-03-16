-- list all records of the table
-- Not list records without a name value
-- descending score

SELECT
    score, name
FROM
    second_table
WHERE
    name IS NOT NULL
ORDER BY
    score DESC;
