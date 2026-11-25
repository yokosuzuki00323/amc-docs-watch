# Amazon Marketing Cloud SQL basics | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/amc-sql/basics

# AMC SQL basics

Was this page helpful?## SELECT

The `SELECT` statement is used to select records from a table.

```
SELECT <column1>, <column2>, ...
FROM <table1>
```
* \<column1\>, \<column2\> refer to the field names in the table
* \<table1\> refers to the table name that you want to select data from

 Note AMC does not support selecting all columns from a table (`SELECT *`) due to privacy reasons## DISTINCT

The `SELECT DISTINCT` statement is used to return only distinct (unique)
values from a column in a database.

```
SELECT DISTINCT <column1>, <column2>, ...
FROM <table1>
```
* \<column1\>, \<column2\> refer to the field names in the table
* \<table1\> refers to the table name that you want to select data from

## FROM

The `FROM` statement is used to specify the table to select the data from.

```
SELECT DISTINCT <column1>, <column2>, ...
FROM <table1>
```
* \<column1\>, \<column2\> refer to the field names in the table
* \<table1\> refers to the table name that you want to select data from

## LIMIT

The `LIMIT` clause restricts the number of rows returned by a SQL query. It is commonly used for sampling data or retrieving top results.

```
SELECT column1, column2, ...
FROM table_name
WHERE condition
GROUP BY column1, column2, ...
LIMIT number;
```
* `LIMIT` specifies the maximum number of rows to return
* Always applied after filtering (`WHERE`)
* Returns the first N rows from the result set

## JOIN

AMC supports the `JOIN` clause which combines rows from two or more
tables, based on a matching column between them.

```
SELECT <table1>.<column1>, <table2>.<column2>, <table2>.<column1>,....
FROM table1
JOIN table2
ON <table1>.<matching_column1> = <table2>.<matching_column2>
```
* \<table1\> refers to the first table
* \<column1\> refers to a column in the first table
* \<table2\> refers to the second table
* \<column2\> refers to a column in the second table
* \<matching\_column1\> refers to a column in table1 that should be used to match with a column in table2
* \<matching\_column2\> refers to a column in table 2 that should be used to match with a column in table1

## Supported JOIN clauses

The types of `JOIN` clauses that AMC supports are:

* **Inner Join / Join**

This `JOIN` returns only the matching rows from both the tables in the `JOIN`.

* **Left Join/ Left Outer Join**

This `JOIN` returns all the rows of the table on the left side of the join and matching rows for the table on the right side of the join. For the rows that do not match, it will return `NULL` as the matched values.

* **Right Join / Right Outer Join**

This `JOIN` returns all the rows of the table on the right side of the join and matching rows for the table on the left side of the join. For the rows that do not match, it will return `NULL` as the matched values. See [RIGHT JOIN](/API/docs/en-us/guides/amazon-marketing-cloud/amc-sql/basics#right-join) for more detail.

* **Left Semi Join**

A `LEFT SEMI JOIN` returns rows from the left relation for which at least one matching row exists in the right relation. Right\-input columns are not projected in the output. The `LEFT` prefix is required.

```
SELECT t.* FROM t LEFT SEMI JOIN s ON t.id = s.id
```
* **Left Anti Join**

A `LEFT ANTI JOIN` returns rows from the left relation for which no matching row exists in the right relation. Right\-input columns are not projected. The `LEFT` prefix is required.

```
SELECT t.* FROM t LEFT ANTI JOIN s ON t.id = s.id
```
* **Full Outer Join**

This `JOIN` returns all the matched and unmatched rows from both the tables. For the rows that do not match, it will return `NULL` as the
matched values.

* **Cross Join**

A `CROSS JOIN` returns the cartesian product of the rows from the tables that are joined.

* **Non\-Equi Join**

A Non\-Equi `JOIN` retrieves data from multiple tables by matching column values between them based on an inequality operator like \>, \<, !\= etc.

Syntax

```
SELECT <table1>.<column1>, <table2>.<column2>, <table2>.<column1>,....
FROM table1
JOIN table2
ON <table1>.<matching_column1> [> | <| >= | <=] <table2>.<matching_column2>
```
* \<table1\> refers to the first table
* \<column1\> refers to a column in the first table
* \<table2\> refers to the second table
* \<column2\> refers to a column in the second table
* \<matching\_column1\> refers to a column in table1 that should be used to match with a column in table2
* \<matching\_column2\> refers to a column in table 2 that should be used to match with a column in table1

## JOIN vs UNION

`JOIN` clause combines rows from two or more tables, based on a matched column between them.

`UNION` clause combines the results obtained from two queries.

### Differences between `JOIN` and `UNION` clause

| `JOIN` | `UNION` |
| --- | --- |
| Combines rows from two or more tables, based on a matched column between them | Combines results of two or more queries or `SELECT` statements |
| The two or more tables used in the `JOIN` may have different columns, with one or more foreign keys for JOINing to each other that are based on defined conditions. | The two or more `SELECT` statements used in the `UNION` should have the same number and data type of columns |
| The result set may have more columns as the `JOIN` tries to match and retrieve data from the JOINed table. If a row from the first table has keys that match multiple rows in the second table, there will be a row in the Example Query Results table for each combination. The result set may or may not have the same number of rows as the tables used in the `JOIN` | A `UNION` will have all the rows from the first data source \+ all the rows from the second. Hence, the result set will have more rows, but the same set of columns, as the `UNION` consolidates the data in a single set. `UNION` keeps unique records. `UNION ALL` keeps all records, including duplicate records |

## WHERE

The `WHERE` clause is used to filter the query results based on a
condition.

```
SELECT <column1>, <column2>, ...
FROM <table1>
WHERE <condition>
```
* \<column1\>, \<column2\>\\ refer to the field names in the table that you want to select data from
* \<table1\> refers to the table name
* \<condition\> refers to the condition that should be true to filter down the query results

## GROUP BY

The `GROUP BY` statement is used with aggregate functions `MIN()`, `MAX()`,
`SUM()`, `AVG()` etc. to group the data by one or more columns.

```
SELECT <column1>, <FUNC>( <column2>), ...
FROM <table1>
WHERE <condition1>
GROUP BY <column1>
```
* \<column1\>, \<column2\> refer to the field names in the table that you
want to select data from
* \<table1\> refers to the table name
* \<FUNC\> refers to an aggregated function like `MIN()`, `MAX()` etc.
* \<condition1\> refers to the condition that should be true to filter
down the query results

## HAVING

The `HAVING` clause is similar to the `WHERE` clause as it helps filter the
data based on specific conditions. `HAVING` clause can be used with
aggregate functions, but a `WHERE` clause cannot be used.

```
SELECT <column1>, <FUNC>( <column2>), ...
FROM <table1>
WHERE <condition1>
GROUP BY <column1>
HAVING <condition2>
```
* \<column1\>, \<column2\> refer to the field names in the table that you
want to select data from
* \<table1\> refers to the table name
* \<FUNC\> refers to an aggregated function like `MIN()`, `MAX()` etc.
* \<condition1\> and \<condition2\> refer to the condition that should be
true to filter down the query results

## ALIASES

Aliases are used to give a table, or a column, a temporary name.

```
SELECT <column1> as <alias_name1>, <column2>, ...
FROM <table1> <alias_name2>
```
* \<column1\>, \<column2\> refer to the field names in the table that you want to select data from
* \<table1\> refers to the table name

## VALUES

The `VALUES` command specifies the values to include in a common table
expression. Use [Common Table Expressions](/API/docs/en-us/guides/amazon-marketing-cloud/amc-sql/basics#common-table-expression) to
define values to filter the queries.

```
WITH <table1> ( <column1>) AS (
  VALUES
    (<value1>),
    (<value2>),
    (<value3>)
)
```
* \<column1\> refers to the field names in the table
* \<table1\> refers to the temporary table name
* \<value1\>, \<value2\> etc. refers to the values that will be included
in the table

## REGEX

Regex or Regular Expressions, is a sequence of characters that are used
to construct search strings or patterns that can be used for filtering
data. A Regex can be a combination of integers, special characters etc.

| Pattern | Usage | Example | Explanation |
| --- | --- | --- | --- |
| ^ | Begins with | ^Toast | Begins with toast. Example: toaster |
| (?!) | Case Insensitive | (?!)consideration | This will match with Consideration, CONSIDERATION, conSIDerATION |
| ‘ | Escape single quote | men''s electric shaver | This will match men’s electric shaver |
| " | Escape double quote | red 48'''' rod | This will match red 48" rod |

## COMMON TABLE EXPRESSION

A Common Table Expression or a CTE is a temporary result set derived
using a query, which can then be referenced in a `SELECT` statement as a
table. Note that there is a comma separating multiple CTE definitions
and no comma prior to the terminal query.

```
WITH <cte_name1>
AS (<query>),

<cte_name2>
AS (<query>)
SELECT <column1>,<column2>
FROM <cte_name>
```
* \<cte\_name\> refers to the name of the temporary table
* \<query\> refers to the query used to derive the result set

## Query syntax

### RIGHT JOIN

AMC supports `RIGHT JOIN`, which joins two relations and returns all rows from the right relation and matching rows from the left.

```
SELECT ... FROM left_table RIGHT [OUTER] JOIN right_table ON condition
```
### INTERSECT / INTERSECT DISTINCT

`INTERSECT` returns rows that appear in both query results. `INTERSECT ALL` is not supported.

```
query1 INTERSECT DISTINCT query2
```
### EXCEPT / EXCEPT DISTINCT / MINUS

`EXCEPT` returns rows from the first query that do not appear in the second. `EXCEPT ALL` is not supported. `MINUS` is an alias for `EXCEPT`.

```
query1 EXCEPT DISTINCT query2
query1 MINUS query2
```
### GROUPING SETS

`GROUPING SETS` groups rows by multiple grouping combinations in a single query. Maximum 32 total grouping sets. The `GROUPING()` function (to identify which columns are aggregated in a given output row) is not supported.

```
GROUP BY GROUPING SETS ((col1, col2), (col1), ())
```
### ROLLUP

`ROLLUP` generates subtotal rows for a hierarchy of grouping columns. It is equivalent to a sequence of `GROUPING SETS` from the most to the least granular. Maximum 32 total grouping sets. The `GROUPING()` function is not supported.

```
GROUP BY ROLLUP (col1, col2, col3)
```
### CUBE

`CUBE` generates subtotal rows for all combinations of grouping columns. Maximum 32 total grouping sets — a wide `CUBE` can reach this limit quickly. The `GROUPING()` function is not supported.

```
GROUP BY CUBE (col1, col2, col3)
```
### Correlated subqueries (EXISTS / NOT EXISTS / IN)

Correlated `EXISTS`, `NOT EXISTS`, and `IN` subqueries are supported. Correlated `NOT IN` subqueries and correlated scalar subqueries (a subquery used as a single value, outside `EXISTS`/`IN`) are not supported.

 Note `value` is a reserved word in AMC SQL — using a column literally named `value` (for example, `s.value`) will not parse. Use a different column name.
```
SELECT * FROM t WHERE EXISTS (SELECT 1 FROM s WHERE s.id = t.id)
SELECT * FROM t WHERE t.id IN (SELECT id FROM s WHERE s.amount > 100)
```
