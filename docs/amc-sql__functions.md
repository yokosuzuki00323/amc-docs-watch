# Amazon Marketing Cloud SQL functions | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/amc-sql/functions

# AMC SQL functions

Was this page helpful?## String functions

### BTRIM

Removes leading and trailing characters from a string. If no characters are specified, removes spaces.

```
BTRIM(string)
BTRIM(string, chars)
```
* `string` the input string
* `chars` (optional) a string of characters to trim

```
SELECT BTRIM('  hello  ') -- returns 'hello'
SELECT BTRIM('xxhelloxx', 'x') -- returns 'hello'
```
### CHARINDEX

Searches for a substring within a string and returns its starting position, with optional start position parameter for refined searches.

```
CHARINDEX(substring, string [, start_position])
```
### CONCAT

The `CONCAT` function concatenates multiple strings and returns the result as a single string. All inputs will be cast to string data type for joining.

```
CONCAT(expression [, expression]*)
```
### FORMAT

Formats a value according to a specified pattern, allowing custom string representation of numbers, dates, and other types

```
FORMAT(format_string, value, ...)
```
* `format_string` a format string using `%s`, `%d`, `%f`, etc.
* `value, ...` values to substitute into the format string

```
SELECT FORMAT('Hello, %s! You have %d messages.', 'Alice', 5)
-- returns 'Hello, Alice! You have 5 messages.'
```
### FORMAT\_STRING

Alias for `FORMAT`.

```
FORMAT_STRING(format_string, value, ...)
```
### INSTR

Finds the first occurrence position of a substring within a string, returning 0 if not found. Similar to `POSITION`, but with a different syntax.

```
INSTR(string, substring)
```
### LEFT

Extracts a specified number of characters from the left side of a string

```
LEFT(string, length)
```
### LENGTH

Calculates the number of characters in a string, including spaces and special characters

```
LENGTH(string)
```
### LIKE

AMC supports the `LIKE` operator which matches a column name to a string value specified by the user. `LIKE` does not require regex syntax and works with wildcards.

```
<column1> LIKE <expression>
```
* `column1` specifies the column that is in the `WHERE` clause that needs to be checked for a condition.
* `expression` refers to the expression or value that the column needs to be compared to.

### LOCATE

Alias of `CHARINDEX`.

```
LOCATE(substring, string[, start_position])
```
### LOWER

Converts all characters in a string to lowercase, useful for case\-insensitive comparisons

```
LOWER(string)
```
### LPAD

The `LPAD` function pads a string on the left side to a specified total length. If the string is already longer than the specified length, it is truncated to fit.

```
LPAD(string, length [, pad_string])
```
* `string` the input string to pad
* `length` the desired total length of the resulting string
* `pad_string` (optional) the characters to use for padding. Default is a space character.

### LTRIM

Removes leading whitespace characters from the beginning of a string

```
LTRIM(string)
```
### POSITION

Finds the first occurrence position of a substring within a string, returning 0 if not found

```
POSITION(substring IN string)
```
### REGEXP\_COUNT

Returns the number of times a pattern matches in a string.

```
REGEXP_COUNT(string, pattern)
```
* `string` the input string
* `pattern` a regular expression pattern

```
SELECT REGEXP_COUNT('banana', 'a') -- returns 3
```
### REGEXP\_INSTR

Returns the position of the first match of a regular expression pattern in a string. Only the two\-argument form is supported; the three\-argument form is not supported.

```
REGEXP_INSTR(string, pattern)
```
* `string` the input string
* `pattern` a regular expression pattern

Returns a 1\-based position, or `0` if there is no match.

```
SELECT REGEXP_INSTR('hello world', 'w') -- returns 7
```
### REGEXP\_REPLACE

Replaces text matching a regular expression pattern with specified replacement text

```
REGEXP_REPLACE(string, pattern, replacement)
```
### REGEXP\_SUBSTR

Extracts substring matching a regular expression pattern from a string

```
REGEXP_SUBSTR(string, pattern)
```
### REGEXP\_SPLIT

The `REGEXP_SPLIT` function splits an input string into a collection of substrings, using a regular expression pattern occurrence to split the string.

```
REGEXP(<string>,<pattern>)
```
* `<string>` The input string that will be split into a collection of substrings
* `<pattern>` The regular expression pattern that is matched to split the string.

### REPEAT

The `REPEAT` function repeats a string a specified number of times and returns the concatenated result.

```
REPEAT(string, count)
```
* `string` the input string to repeat
* `count` the number of times to repeat the string. If 0 or negative, returns an empty string.

### REPLACE

Substitutes all occurrences of a search string with a replacement string within text

```
REPLACE(string, search, replacement)
```
### REVERSE

Returns a string with the characters in reverse order.

```
REVERSE(string)
```
* `string` the string to reverse

```
SELECT REVERSE('hello') -- returns 'olleh'
```
### RIGHT

Extracts a specified number of characters from the right side of a string, useful for suffix extraction

```
RIGHT(string, length)
```
### RLIKE / NOT RLIKE

Tests whether a string matches a regular expression pattern. Infix operator.

```
string RLIKE pattern
string NOT RLIKE pattern
```
* `string` the input string
* `pattern` a regular expression pattern

```
SELECT 'hello' RLIKE 'h.*o' -- returns true
SELECT 'hello' NOT RLIKE '^w' -- returns true
```
### RPAD

The `RPAD` function pads a string on the right side to a specified total length. If the string is already longer than the specified length, it is truncated to fit.

```
RPAD(string, length [, pad_string])
```
* `string` the input string to pad
* `length` the desired total length of the resulting string
* `pad_string` (optional) the characters to use for padding. Default is a space character.

### RTRIM

Removes trailing whitespace characters from the end of a string, complementing `LTRIM`

```
RTRIM(string)
```
### SIMILAR TO

The `SIMILAR TO` expression evaluates to true only if the value matches the provided regular expression. The regular expression should follow Java regular expression syntax. Both inputs must be strings. The results returned are in a Boolean value.

```
expression [NOT] SIMILAR TO expression
```
### SPLIT

Splits a string by a regular expression pattern and returns an array of substrings. Alias for `REGEXP_SPLIT`.

```
SPLIT(string, pattern)
```
* `string` the input string
* `pattern` a regular expression pattern

```
SELECT SPLIT('a1b2c', '[0-9]') -- returns ['a', 'b', 'c']
```
### SPLIT\_PART

Splits a string by a delimiter and returns the part at the specified position.

```
SPLIT_PART(string, delimiter, index)
```
* `string` the input string
* `delimiter` the delimiter string; supports dynamic (non\-literal, column\-valued) values
* `index` the 1\-based position of the part to return; supports dynamic (non\-literal) values and negative indexes (counts from the end). Index `0` is rejected; indexes outside the 32\-bit integer range are rejected.

```
SELECT SPLIT_PART('a,b,c', ',', 2) -- returns 'b'
SELECT SPLIT_PART('a,b,c', ',', -1) -- returns 'c'
```
### STRPOS

Returns the position of a substring within a string, similar to `INSTR` but with different syntax.

```
STRPOS(string, substring)
```
### STR*TO*MAP

Converts a delimited string into a key\-value map structure using specified delimiters. The pair and key\-value delimiters are optional.

```
STR_TO_MAP(string)
STR_TO_MAP(string, pair_delimiter)
STR_TO_MAP(string, pair_delimiter, key_value_delimiter)
```
* `string` the input string
* `pair_delimiter` (optional) delimiter between key\-value pairs; default `,`
* `key_value_delimiter` (optional) delimiter between keys and values; default `:`

 Note With the CSV output format, the final output of a query cannot contain a `MAP` column. You can use map values anywhere else in the query. To output a map, index into it (for example `m['key']`) or wrap it in `TO_JSON()`.
```
SELECT STR_TO_MAP('a:1,b:2,c:3')['b'] -- returns '2'
```
### SUBSTRING

Extracts a portion of a string based on starting position and optional length

```
SUBSTRING(string FROM start [FOR length])
```
### TRANSLATE

Replaces characters in a string based on a character mapping.

```
TRANSLATE(string, from, to)
```
* `string` the input string
* `from` characters to replace
* `to` replacement characters, matched by position to `from`

```
SELECT TRANSLATE('hello', 'el', 'ip') -- returns 'hippo'
```
### TRIM

The `TRIM()` function removes the space character or other specified characters from the start or end of a string. This function is useful when working with strings like advertiser or campaign names.

To remove the leading and trailing space characters from str:

```
TRIM(str)
```
To remove the leading and trailing trimStr characters from str:

```
TRIM(BOTH trimStr FROM str)
```
To remove the leading trimStr characters from str:

```
TRIM(LEADING trimStr FROM str)
```
To remove the trailing trimStr characters from str:

```
TRIM(TRAILING trimStr FROM str)
```
### UPPER

Converts all characters in a string to uppercase, useful for case normalization

```
UPPER(string)
```
### \|\| (String concatenation)

Concatenates two strings. Rejects array operands — use `ARRAY_CAT` for array concatenation.

```
string1 || string2
```

```
SELECT 'hello' || ' ' || 'world' -- returns 'hello world'
```
## Math functions

### ABS

Returns the absolute value of a numeric expression, converting negative numbers to positive while keeping positive numbers unchanged

```
ABS(numeric_expression)
```
### SIN, COS, TAN, ASIN, ACOS, ATAN, COT

Trigonometric functions operating on radians.

```
SIN(x)
COS(x)
TAN(x)
ASIN(x)
ACOS(x)
ATAN(x)
COT(x)
```
* `x` a numeric value in radians

```
SELECT SIN(PI() / 2) -- returns 1.0
SELECT DEGREES(ACOS(-1)) -- returns 180.0
```
### ATAN2

Returns the angle in radians between the positive x\-axis and the point (x, y).

```
ATAN2(y, x)
```
### CBRT

Returns the cube root of a number.

```
CBRT(x)
```
### CEIL

Rounds a number up to the nearest integer, returning the smallest integer greater than or equal to the input

```
CEIL(number)
```
### DEGREES

Converts radians to degrees.

```
DEGREES(x)
```
### DIV

Returns the integer quotient of a division, truncating toward zero. Requires integral or `DECIMAL(p,0)` operands. Division by zero gives `NULL`.

```
DIV(a, b)
```

```
SELECT DIV(7, 2) -- returns 3
SELECT DIV(-7, 2) -- returns -3
SELECT DIV(7, 0) -- returns NULL
```
### E()

Returns the mathematical constant e (approximately 2\.71828\), used in exponential and natural logarithm calculations

```
E()
```
### EXP

Calculates e raised to the power of the input value, the inverse of the natural logarithm function

```
EXP(number)
```
### FLOOR

Rounds a number down to the nearest integer, returning the largest integer less than or equal to the input value

```
FLOOR(number)
```
### LN

Calculates the natural logarithm (base e) of a number, the inverse of the `EXP` function.

```
LN(number)
```
### LOG

Calculates the logarithm of a number with a specified base, generalizing logarithmic calculations

```
LOG(base, number)
```
### LOG10

Calculates the base\-10 logarithm of a number, commonly used for decimal scale calculations

```
LOG10(number)
```
### PI

Returns the mathematical constant π (pi).

```
PI()
```
### RADIANS

Converts degrees to radians.

```
RADIANS(x)
```
### POWER

Raises a number to the specified power, enabling exponential calculations

```
POWER(number, power)
```
### RANDOM

Generates a pseudo\-random decimal number between 0 (inclusive) and 1 (exclusive). `RAND` is an alias for `RANDOM`. The seeded form (`RAND(seed)`) is not supported.

```
RANDOM()
RAND()
```
### ROUND

The `ROUND` function rounds numeric values to the specified decimal point. The result of input expression must be a numeric data type. If no rounding is specified, the result will default to 0\.

```
ROUND(expression [, integer])
```
### SIGN

The `SIGN` function returns the sign of a numeric expression as \-1, 0, or 1, indicating whether the number is negative, zero, or positive respectively.

```
SIGN(numeric_expression)
```
* `numeric_expression` a numeric value (integer, decimal, or floating\-point)

### SQRT

Calculates the square root of a non\-negative number, returning `NULL` for negative inputs

```
SQRT(number)
```
### TRUNC

Truncates a number to specified decimal places without rounding

```
TRUNC(number[, decimals])
```
## Aggregate functions

### APPROX\_COUNT\_DISTINCT

The `APPROX_COUNT_DISTINCT` function returns an approximate count of distinct non\-null values in a column. It provides faster performance than `COUNT(DISTINCT)` for large data sets, with a small margin of error.

```
APPROX_COUNT_DISTINCT(column_name)
```
* `column_name` refers to the column in the table that the function will operate on and return the approximate count of distinct values.

### ANY\_VALUE

Returns an arbitrary value from the group. Nondeterministic — may return `NULL`. Supported as both an aggregate function and a window function.

```
ANY_VALUE(expr)
```
### BOOL\_AND

Returns `true` if all values in the group are `true`. Supported as both an aggregate function and a window function.

```
BOOL_AND(boolean_expr)
```
### BOOL\_OR

Returns `true` if any value in the group is `true`. Supported as both an aggregate function and a window function.

```
BOOL_OR(boolean_expr)
```
### AVG

Returns the average of values (arithmetic mean) in columns. This function works with numeric data type as input and ignores null values.
If all input values are null, the function returns a `NULL` result.

```
AVG(column_name)
```
* \<column\_name\> refers to the column in the table that the function will operate on and return the arithmetic mean of the values.

### COUNT

```
COUNT( [ALL | DISTINCT] column )
```
Total number of values in column. `ALL` is the default. When `DISTINCT` is specified, it eliminates all duplicate values. However, `DISTINCT` cannot be specified to get the total number of non\-null values.

```
COUNT(column_name)
```
or

```
COUNT(DISTINCT column_name)
```
* \<column\_name\> refers to the column in the table that the function will operate on.

### COLLECT\_SORTED

The `COLLECT_SORTED` function creates a sorted array of all non\-null input values. Unlike `COLLECT` followed by `ARRAY_SORT`, this function performs collection and sorting in a single step.

```
COLLECT_SORTED(column_name)
```
* `column_name` refers to the column in the table that the function will operate on and return a sorted array of values.

### COLLECT\_LIST

Returns an array of all values in the group, including duplicates. Same as `COLLECT(x)`. `DISTINCT` is not supported. Does not work with `OVER` (not supported as a window function). Element order is not guaranteed.

```
COLLECT_LIST(expr)
```
### COLLECT\_SET

Returns an array of distinct values in the group. Same as `COLLECT(DISTINCT x)`. `DISTINCT` is not supported as a modifier on `COLLECT_SET` itself (distinctness is implied by the function). Does not work with `OVER` (not supported as a window function). Element order is not guaranteed.

```
COLLECT_SET(expr)
```
### MIN

The `MIN` function returns the minimum value in a set of rows. Null values will not be considered. The result will be null if all input values are null.

```
MIN(column_name)
```
* \<column\_name\> refers to the column in the table that the function will operate on and return the minimum value.

### MAX

The `MAX` function returns the maximum value of all inputs. Null values will not be considered. The result will be null if all input values are
null.

```
MAX(column_name)
```
* \<column\_name\> refers to the column in the table that the function will operate on and return the maximum value.

### SUM

Returns the sum of all values in the column (or expression). This function works with numeric data type and ignores null values. If all
input values are null, `SUM()` returns null.

```
SUM(column_name)
```
* \<column\_name\> refers to the column in the table that the function will operate on and return the sum of the values in it.

### HLL*SKETCH*AGG

Aggregates values into a HyperLogLog (HLL) sketch for approximate distinct count estimation. Accepts INTEGER, STRING, or BINARY input; `DECIMAL` and `DOUBLE` are rejected. Also works as a window function with `OVER (PARTITION BY ...)` only — no `ORDER BY` or frame clause.

 Note The final output of a query cannot contain an HLL sketch, also when it is converted with `BASE64` or `HEX`. To output a count, use `HLL_SKETCH_ESTIMATE`.
```
HLL_SKETCH_AGG(expr)
HLL_SKETCH_AGG(expr, lgConfigK)
```
* `expr` the value to aggregate; INTEGER, STRING, or BINARY only
* `lgConfigK` (optional) log\-base\-2 of the sketch size; must be a literal integer in the range 4–21

### HLL*SKETCH*ESTIMATE

Returns the approximate distinct count estimate from an HLL sketch.

```
HLL_SKETCH_ESTIMATE(sketch)
```
* `sketch` a binary HLL sketch value, typically produced by `HLL_SKETCH_AGG` or `HLL_UNION_AGG`

### HLL\_UNION

Returns the union of two HLL sketches as a new sketch.

```
HLL_UNION(s1, s2)
HLL_UNION(s1, s2, allowDifferentLgConfigK)
```
* `s1`, `s2` binary HLL sketch values to union
* `allowDifferentLgConfigK` (optional) a literal BOOLEAN; when `true`, allows unioning sketches built with different `lgConfigK` values

### HLL*UNION*AGG

Aggregates a column of HLL sketches into a single unioned sketch. Also works as a window function with `OVER (PARTITION BY ...)` only — no `ORDER BY` or frame clause.

```
HLL_UNION_AGG(sketch)
HLL_UNION_AGG(sketch, allowDifferentLgConfigK)
```
* `sketch` a binary HLL sketch value for each row in the group
* `allowDifferentLgConfigK` (optional) a literal BOOLEAN; when `true`, allows unioning sketches built with different `lgConfigK` values

## Date/Time functions

### CONVERT\_TIME\_ZONE

The `CONVERT_TIME_ZONE` function converts a timestamp from one time zone to another. Unlike `CONVERT_TIME_ZONE_FROM_UTC` which assumes the input is in UTC, this function allows specifying both the source and destination time zones.

```
CONVERT_TIME_ZONE(inputTime, 'sourceTimeZone', 'destinationTimeZone')
```
* `inputTime` refers to the timestamp to convert
* `sourceTimeZone` the time zone of the input timestamp (tz database name format)
* `destinationTimeZone` the target time zone for the output (tz database name format)

### CONVERT\_TIMEZONE

Converts a timestamp from one time zone to another. This is distinct from `CONVERT_TIME_ZONE` above — the argument order differs and the timestamp argument is last, not first. Passing it first compiles but silently returns NULL with no error. The two\-argument form converts from UTC; the three\-argument form specifies an explicit source time zone.

```
CONVERT_TIMEZONE(target_tz, ts)
CONVERT_TIMEZONE(source_tz, target_tz, ts)
```
### CONVERT TIME ZONE FROM UTC

Given a time data type, this function converts UTC timestamp to the timestamp of the specified time zone. The input can either be a
`TIMESTAMP` or `DATE` data type and the result will match the data type of the input. The input time zone follows tz database name format.

```
CONVERT_TIME_ZONE_FROM_UTC(inputTime, 'timeZone')
```
* \<inputTime\> refers to the timestamp in UTC
* \<timezone\> The time zone for the new timestamp.

### FROM*UTC*TIMESTAMP

Converts a UTC timestamp to a target time zone. Alias for `CONVERT_TIME_ZONE_FROM_UTC`.

```
FROM_UTC_TIMESTAMP(ts, timezone)
```
### CURRENT\_DATE

Returns the current date in UTC, commonly used for date\-based comparisons and calculations

```
CURRENT_DATE
```
### CURRENT\_TIMESTAMP

Returns the current date and time in UTC, providing precise temporal information

```
CURRENT_TIMESTAMP
```
### DATE\_DIFF

Returns the number of days between two dates.

```
DATE_DIFF(end_date, start_date)
```

```
SELECT DATE_DIFF(DATE '2026-09-01', DATE '2026-08-01') -- returns 31
```
### DATE\_PART

Extracts a date/time field from a timestamp using a string\-named field. Returns the same values as `EXTRACT`, but takes the field name as a string.

```
DATE_PART(part_string, timestamp)
```
* `part_string` the field to extract (for example, `'year'`, `'month'`, `'day'`, `'quarter'`, `'doy'` or `'day_of_year'`). `'dayofyear'` is rejected — use `'doy'` or `'day_of_year'` instead.
* `timestamp` a TIMESTAMP or DATE value

```
SELECT DATE_PART('quarter', TIMESTAMP '2026-08-15 00:00:00') -- returns 3
```
### DATE\_TRUNC

The `DATE_TRUNC` function truncates the input timestamp to a specified level of granularity. Granularity must be single quoted and valid
formats can be `SECOND`, `MINUTE`, `HOUR`, `DAY`, `WEEK`, `MONTH`, `QUARTER`, `YEAR`.

```
DATE_TRUNC('granularity', inputTime)
```
* \<granularity\> refers to the date part to which to truncate the timestamp value
* \<inputTime\> refers to the timestamp to truncate

### DAY, DAYOFYEAR, QUARTER

Standalone function forms for date\-part extraction, distinct from the `EXTRACT(... FROM ...)` syntax — these take the date/timestamp directly as a function argument. `DAY(x)` is a function call form, separate from the `EXTRACT(DAY FROM ...)` field keyword.

```
DAY(x)
DAYOFYEAR(x)
QUARTER(x)
```
* `x` a TIMESTAMP or DATE value

```
SELECT DAY(DATE '2026-08-15')       -- returns 15
SELECT DAYOFYEAR(DATE '2026-08-15') -- returns 227
SELECT QUARTER(DATE '2026-08-15')   -- returns 3
```
### DAYOFMONTH

Returns the day of the month as a number between 1 and 31

```
DAYOFMONTH(date)
```
### DAYOFWEEK

Returns a number representing the day of the week (1\-7, where 1 is Sunday), useful for weekday\-based logic

```
DAYOFWEEK(date)
```
### EPOCH TO UTC TIMESTAMP

This function returns the timestamp value with epoch as input time. The input can result in seconds or milliseconds and the result will assume one or the other based on the magnitude.

```
EPOCH_TO_UTC_TIMESTAMP(expression)
```
* \<expression\> refers to the arguments passed to the function.

The function will produce a timestamp value from the input time

### EXTEND\_TIME\_WINDOW

The `EXTEND_TIME_WINDOW` function allows for the time period of the input tables to be extended beyond the reporting time window.

```
EXTEND_TIME_WINDOW( <table_name>, <Number_of_Days_Retro>, <Number_of_Days_Future> )
```
* \<`table_name`\> refers to the table that needs to be extended beyond the current timeframe of the query
* \<`Number_of_Days_Retro`\> refers to the Number of Days to extend the table retroactively to pull data from
* \<`Number_of_Days_Future`\> refers to the Number of Days to extend the table in the future, beyond the current timeframe of the query

`EXTEND_TIME_WINDOW` is query\-scoped: once applied to a table in any CTE, the extended window carries forward to all subsequent references to that table in the query. To restrict a specific CTE to the standard reporting period, add an explicit date filter:

```
WHERE event_dt_utc >= BUILT_IN_PARAMETER('TIME_WINDOW_START')
  AND event_dt_utc < BUILT_IN_PARAMETER('TIME_WINDOW_END')
```
### EXTRACT

The `EXTRACT` function extracts one time unit from a `DATE` or `TIMESTAMP` value. The time unit can be one of `SECOND`, `MINUTE`, `HOUR`, `DAY`, `DOW`, `WEEK`, `MONTH`, `QUARTER`, `YEAR`, `DAYOFYEAR`/`DOY`.

```
EXTRACT(timeUnit FROM expression)
EXTRACT(QUARTER FROM timestamp)
EXTRACT(DAYOFYEAR FROM timestamp)
```
* \<timeUnit\> refers to the specific date part in the column or expression of data type of `TIMESTAMP`
* `QUARTER` calendar quarter (1–4\)
* `DAYOFYEAR` / `DOY` day number within the year. `DAY_OF_YEAR` is rejected — use `DAYOFYEAR` or `DOY` instead.

### FLOOR (temporal)

Truncates a datetime value to the nearest lower boundary of the specified unit. Alias for `DATE_TRUNC`. This is distinct from the numeric `FLOOR` in Math functions above.

```
FLOOR(datetime TO unit)
```
* `unit` one of: `SECOND`, `MINUTE`, `HOUR`, `DAY`, `WEEK`, `MONTH`, `QUARTER`, `YEAR`

Returns the same type as the input (a DATE input returns a DATE; a TIMESTAMP input returns a TIMESTAMP).

```
SELECT FLOOR(TIMESTAMP '2026-08-15 14:32:00' TO MONTH)
-- returns 2026-08-01 00:00:00
```
### HOUR

Extracts the hour component (0\-23\) from a timestamp, useful for time\-based analysis

```
HOUR(timestamp)
```
### MINUTE

Extracts the minute component (0\-59\) from a timestamp value

```
MINUTE(timestamp)
```
### MONTH

Extracts the month number (1\-12\) from a date value

```
MONTH(date)
```
### SECOND

Extracts the seconds component (0\-59\) from a timestamp value

```
SECOND(timestamp)
```
### WEEK

Returns the week number (1\-53\) of a given date

```
WEEK(date)
```
### YEAR

Extracts the year component from a date value

```
YEAR(date)
```
### TIMESTAMP (single\-argument cast)

Converts a string to a TIMESTAMP. Single\-argument cast alias.

```
TIMESTAMP(string)
```
### TO\_CHAR

Converts a numeric value to a string using a format pattern. Datetime values are rejected.

```
TO_CHAR(expr, format)
```
* `expr` a numeric value
* `format` a string literal format pattern

```
SELECT TO_CHAR(1234567.89, '999,999,999.99') -- returns '1,234,567.89'
```
### TO\_DATE

Converts a string or expression to a DATE. Supports an optional format string.

```
TO_DATE(string)
TO_DATE(string, format)
```
* `string` a date string
* `format` (optional) a format pattern (for example, `'yyyy-MM-dd'`); must be a string literal

### TO\_NUMBER

Converts a string to a numeric value using a format pattern.

```
TO_NUMBER(expr, format)
```
* `expr` a string representation of a number
* `format` a numeric format pattern that defines result precision and scale

### TO\_TIMESTAMP

Converts a string or expression to a TIMESTAMP. Supports an optional format string.

```
TO_TIMESTAMP(string)
TO_TIMESTAMP(string, format)
```
* `string` a timestamp string
* `format` (optional) a format pattern; must be a string literal

### SECONDS BETWEEN

The `SECONDS_BETWEEN` function calculates the time difference in seconds between two datetime values. It returns the number of seconds from firstInputTime to secondInputTime, computed as `secondInputTime`minus `firstInputTime`.

```
SECONDS_BETWEEN(firstInputTime, secondInputTime)
```
## Conditional functions

### CASE

The `CASE` expression is a conditional expression that returns the expression from the first condition that evaluates to true.

```
CASE
  WHEN booleanExpression1 THEN expression1
  WHEN booleanExpression2 THEN expression2
  WHEN booleanExpressionN THEN expressionN
  ELSE expression
END
```
In the above example, each `CASE` expression is compared and evaluated to the booleanExpression and returns the first matching condition. If a match is not found, the `ELSE` clause is returned.

### COALESCE

The `COALESCE` function takes a list of expressions (all of which must be of the same type) and returns the first non\-null argument from the list of inputs. If all of the expressions are null, `COALESCE` returns null.

```
COALESCE(expression [, expression]*)
```
### IF

The `IF` expression evaluates the input boolean value to be true or false based on the supplied expressions values. In the sample syntax below, the expression evaluates and returns trueExpression if the booleanExpression is true, otherwise returns the falseExpression.

```
IF(booleanExpression, trueExpression, falseExpression)
```
### IFNULL

Alias of `COALESCE`.

```
IFNULL(expression, alternate_value)
```
### IN

AMC supports the `IN()` function to specify multiple values in a `WHERE` clause.

```
IN( <value1>, <value2>,..... <valueN> )
```
* \<value1\>, \<value2\>, \<valueN\> are the list of values that the column will be specified in the `WHERE` clause will be compared to. If any of the values match the field, then the `IN` condition will be true.

The `IN()` function can also be used with the `NOT` conditional operator to exclude values

```
NOT IN( <value1>, <value2>,..... <valueN> )
```
### NULLIF

Returns `NULL` if two expressions are equal, otherwise returns the first expression.

```
NULLIF(expr1, expr2)
```
### NVL

Alias of `COALESCE`.

```
NVL(expr1, expr2)
```
### NVL2

Provides three\-way `NULL` logic, returning `expr2` if `expr1` is not null, else returns `expr3`.

```
NVL2(expr1, expr2, expr3)
```
## Array functions

### ARRAY

Constructs an array from a list of values. Both bracket and parenthesis literal syntax are supported, empty or not.

```
ARRAY[value1, value2, ...]
ARRAY(value1, value2, ...)
ARRAY()
```
### ARRAY\_CAT

Concatenates two arrays into a single array, preserving the order of elements from both input arrays.

```
ARRAY_CAT(array1, array2)
```
### ARRAY\_CONTAINS

The `ARRAY_CONTAINS` function returns true if the value is contained in the array. It returns false, if the value is not contained in the array.

```
ARRAY_CONTAINS( <array1>, <value_to_check> )
```
* \<array1\> The source array.
* \<`value_to_check`\> specifies the value that the Array `<array1>` should be checked for

### ARRAY\_COMPLEMENT

Returns an array containing all elements from the first array that do not exist in the second array.

```
ARRAY_COMPLEMENT(array1, array2)
```
### ARRAY\_EXCEPT

Returns elements present in the first array but not in the second. Alias for `ARRAY_COMPLEMENT`, with the same argument order.

```
ARRAY_EXCEPT(array1, array2)
```
### ARRAY\_DISTINCT

Removes duplicate elements from an array while maintaining the order of first occurrence of each element

```
ARRAY_DISTINCT(array)
```
### ARRAY\_INTERSECT

Creates a new array containing only the elements that exist in both input arrays, effectively finding common elements

```
ARRAY_INTERSECT(array1, array2)
```
### ARRAY\_REMOVE

Creates a new array with all occurrences of the specified element removed, maintaining the original order of remaining elements

```
ARRAY_REMOVE(array, element)
```
### ARRAY\_SORT

Use the `ARRAY_SORT()` function to sort the collected values in sequence.

```
SELECT
    ARRAY_SORT(COLLECT(DISTINCT <column1>)) AS column1,
    <column2>
  FROM
    <table>
  GROUP BY
    2
```
### ARRAY\_TO\_STRING

The function `ARRAY_TO_STRING` converts an input array into a string, by concatenating all the elements of the array separated by the separator pattern.

```
ARRAY_TO_STRING(<array>,<separator_pattern>)
```
* \<`array`\> The input array that will be concatenated into a single string
* \<`separator_pattern`\> The pattern that is placed between each element of array in the concatenated string

### ARRAY\_JOIN

Concatenates array elements into a string using a delimiter. Alias for `ARRAY_TO_STRING`.

```
ARRAY_JOIN(array, delimiter)
ARRAY_JOIN(array, delimiter, null_replacement)
```

```
SELECT ARRAY_JOIN(ARRAY['a', 'b', 'c'], ', ') -- returns 'a, b, c'
```
### ARRAY\_UNION

Combines elements from both arrays while removing duplicates, resulting in an array of unique elements from both sources

```
ARRAY_UNION(array1, array2)
```
### CARDINALITY

Counts and returns the total number of elements in an array or map.

```
CARDINALITY(array)
CARDINALITY(map)
```
* `map` a map value

 Note A `NULL` array or map gives `0`.
```
SELECT CARDINALITY(MAP['a', 1, 'b', 2]) -- returns 2
```
### SIZE

Alias for `CARDINALITY`. Works on both arrays and maps. A `NULL` array or map gives `0` — a bare `SIZE(NULL)` with no type context is rejected.

```
SIZE(array)
SIZE(map)
```

```
SELECT SIZE(ARRAY[1, 2, 3]) -- returns 3
```
### COLLECT( \[ALL \| DISTINCT] column name )

The `COLLECT` function creates a list of all non\-unique input values by default. If `DISTINCT` is specified, the output will only contain unique values. Null values are considered in both cases.

```
COLLECT(column_name )
```
or

```
COLLECT( DISTINCT column_name)
```
* \<`column_name`\> refers to the column in the table that the function will operate on and return the list of values.

### EXPLODE

Transforms an array into multiple rows, creating a new row for each element in the input array

```
EXPLODE(array)
```
### FLATTEN

Converts a nested array structure into a single\-level array, simplifying complex array hierarchies

```
FLATTEN(array)
```
## Window functions

Window functions perform calculations over a large set of data, creating windows as columns in aggregate expressions with the following supported operations.

 Note The `OVER` clause is used with window functions and it defines the window specification.### DENSE\_RANK

Similar to `RANK`, but if multiple rows have the same value, they will be assigned the same rank and the following row will have the next
consecutive value. `RANK` would instead assign a non\-consecutive value to rows following ties.

```
DENSE_RANK() OVER window
```
The function takes no argument but requires an empty parenthesis along with the `OVER` clause.

### LAG

The `LAG` function accesses data from a previous row in the result set without using a self\-join. It returns the value of an expression from a row that is a specified number of rows before the current row within a partition.

```
LAG(expression [, offset [, default]]) OVER (PARTITION BY column ORDER BY column)
```
* `expression` refers to the column or expression to return from the previous row
* `offset` (optional) the number of rows back from the current row. Default is 1\.
* `default` (optional) the value returned when the offset goes beyond the partition boundary. Default is `NULL`.

The function requires an `OVER` clause with an `ORDER BY` specification.

### LEAD

The `LEAD` function accesses data from a subsequent row in the result set without using a self\-join. It returns the value of an expression from a row that is a specified number of rows after the current row within a partition.

```
LEAD(expression [, offset [, default]]) OVER (PARTITION BY column ORDER BY column)
```
* `expression` refers to the column or expression to return from the subsequent row
* `offset` (optional) the number of rows forward from the current row. Default is 1\.
* `default` (optional) the value returned when the offset goes beyond the partition boundary. Default is `NULL`.

The function requires an `OVER` clause with an `ORDER BY` specification.

### PARTITION BY

AMC supports the `PARTITION BY` clause which divides the result set into partitions based on the specified column. `PARTITION BY` is generally used with window functions like `SUM()`, `MAX()`, `RANK()` etc. which perform the computation on the windows specified by the `PARTITION BY` clause.

```
SELECT
   <column1>, <window function>
   OVER(
    PARTITION BY <column2>
    [ORDER BY <column3>]
    )
FROM table
```
* \<`window_function`\> specifies the operation that should be performed on the sets of rows within a partition
* \<`column2`\> specifies the field that should be used to partition the rows ORDER BY is the optional clause that can be used within the PARTITION BY clause to sort the rows in a specific order
* \<`column3`\> specifies the field that should be used for sorting the rows

### RANK

Evaluates and returns the rank of a row of values, if all rows in the tables were to be ordered by the elements specified in the `ORDER BY`
clause.

```
RANK() OVER window
```
The function takes no argument but requires an empty parenthesis along
with the `OVER` clause.

### ROW\_NUMBER

Evaluates to the row number based on the ordering of rows specified in the `ORDER BY` clause

```
ROW_NUMBER OVER window
```
The function takes no argument but requires an empty parenthesis along with the `OVER` clause.

### PERCENT\_RANK

Returns the relative rank of a row within its window partition as a value between 0 and 1\.

```
PERCENT_RANK() OVER (PARTITION BY ... ORDER BY ...)
```
### CUME\_DIST

Returns the cumulative distribution of a row within its window partition.

```
CUME_DIST() OVER (PARTITION BY ... ORDER BY ...)
```
### NTILE

Divides the rows in each partition into `n` ranked groups and assigns a group number to each row.

```
NTILE(n) OVER (PARTITION BY ... ORDER BY ...)
```
* `n` a positive integer literal

### FIRST\_VALUE

Returns the first value in the window frame.

```
FIRST_VALUE(expr) OVER (PARTITION BY ... ORDER BY ... [ROWS BETWEEN ... AND ...])
```
 Note `IGNORE NULLS` is not supported.### LAST\_VALUE

Returns the last value in the window frame.

```
LAST_VALUE(expr) OVER (PARTITION BY ... ORDER BY ... [ROWS BETWEEN ... AND ...])
```
 Note `IGNORE NULLS` is not supported.### NTH\_VALUE

Returns the value at a specified position within the window frame.

```
NTH_VALUE(expr, n) OVER (PARTITION BY ... ORDER BY ... [ROWS BETWEEN ... AND ...])
```
* `n` a positive integer literal (1\-based position)

### Window frames (ROWS BETWEEN)

Only `FIRST_VALUE`, `LAST_VALUE`, and `NTH_VALUE` accept a `ROWS BETWEEN` frame, and all three always require an `ORDER BY` clause (not only when a frame is specified). Every other window function (for example `PERCENT_RANK`, `CUME_DIST`, `NTILE`, ranking functions) rejects a frame clause. Frame bounds use non\-negative integer literal offsets. `RANGE BETWEEN` frames are not supported. A frame does not have to include the current row. For example, `ROWS BETWEEN 1 FOLLOWING AND 3 FOLLOWING` and `ROWS BETWEEN 3 PRECEDING AND 1 PRECEDING` are valid. The start of a frame cannot be after its end.

```
FIRST_VALUE(expr) OVER (PARTITION BY ... ORDER BY ...
  ROWS BETWEEN { UNBOUNDED PRECEDING | n PRECEDING | n FOLLOWING | CURRENT ROW }
           AND { CURRENT ROW | n FOLLOWING | n PRECEDING | UNBOUNDED FOLLOWING })
```
## Comparison functions

### GREATEST

The `GREATEST` function returns the largest evaluated expression from a collection of expressions. All expressions must evaluate to numerical data types.

Null will be considered. Result will be null if any input columns value is null.

 Note To work with null values, use the `COALESCE()` function.
```
GREATEST(numericExpression [, numericExpression]*)
```
### LEAST

The `LEAST` function returns the lowest evaluated expression from a collection of expressions. All expressions must evaluate to numerical data types. Null will be considered. Result will be null if any input columns value is null.

 Note To work with null values, use the `COALESCE()` function.
```
LEAST(numericExpression [, numericExpression]*)
```
## Hash functions

### AES\_DECRYPT

Decrypts a value encrypted with `AES_ENCRYPT`. Returns BINARY, not VARCHAR — to get a string, wrap the result in `DECODE(..., 'UTF-8')`. There is no `iv` argument; the IV is embedded in the encrypted payload.

```
AES_DECRYPT(expr, key[, mode[, padding[, aad]]])
```
* `expr` the encrypted value to decrypt
* `key` the encryption key; must match the key used for encryption
* `mode` (optional) one of: `GCM` (default), `CBC`, `ECB`
* `padding` (optional) one of: `DEFAULT` (default), `NONE` (GCM), `PKCS` (CBC/ECB)
* `aad` (optional) additional authenticated data; valid for GCM mode only

```
SELECT DECODE(AES_DECRYPT(encrypted_value, key), 'UTF-8') -- returns the decrypted string
```
### AES\_ENCRYPT

Encrypts a value using the AES algorithm. `mode` and `padding` are optional; defaults are `GCM` and `DEFAULT`.

```
AES_ENCRYPT(expr, key[, mode[, padding[, iv[, aad]]]])
```
* `expr` the value to encrypt
* `key` the encryption key; must be 16, 24, or 32 bytes
* `mode` (optional) one of: `GCM` (default), `CBC`, `ECB`
* `padding` (optional) one of: `DEFAULT` (default), `NONE` (GCM), `PKCS` (CBC/ECB)
* `iv` (optional) initialization vector; GCM: 12 bytes, CBC: 16 bytes
* `aad` (optional) additional authenticated data; valid for GCM mode only

 Note With the CSV output format, the final output of a query cannot contain a `BINARY` column. To output a binary value, wrap it with `BASE64` or `HEX`. To output decrypted text, use `DECODE(..., 'UTF-8')`.### BASE64

Encodes a binary value as a Base64 string.

```
BASE64(binary)
```
### DECODE

Converts a binary value to a string using the specified character set. Supported character sets: `UTF-8`, `US-ASCII`, `ISO-8859-1`, `UTF-16`, `UTF-16BE`, `UTF-16LE`.

```
DECODE(binary, charset)
```
### ENCODE

Converts a string to binary using the specified character set. Supported character sets: `UTF-8`, `US-ASCII`, `ISO-8859-1`, `UTF-16`, `UTF-16BE`, `UTF-16LE`.

```
ENCODE(string, charset)
```
### HASH64

Generates a 64\-bit hash value for the input

```
HASH64(expression)
```
### HEX

Encodes a binary value as a hexadecimal string.

```
HEX(binary)
```
### MD5

Generates a 128\-bit MD5 hash value for a string

```
MD5(string)
```
### SHA1

Generates a 160\-bit SHA\-1 hash value for a string

```
SHA1(string)
```
### SHA2

The `SHA2` function generates a SHA\-256 hash value for a string, providing stronger security than `SHA1` or `MD5`.

```
SHA2(string)
```
* `string` the input value to hash

### UNBASE64

Decodes a Base64\-encoded string to binary.

```
UNBASE64(string)
```
### UNHEX

Decodes a hexadecimal string to binary.

```
UNHEX(string)
```
### XXHASH64

Returns a 64\-bit hash value computed using the xxHash64 algorithm. Takes one argument only — two arguments fail.

```
XXHASH64(expr)
```
* `expr` the value to hash

A `NULL` input gives `NULL`.

```
SELECT XXHASH64('hello') -- returns a BIGINT hash value
```
## VARBINARY functions

### FROM\_VARBINARY

Converts a binary expression into its string representation, useful for working with binary\-encoded data. Supported encoding types: `hex`, `base64`, and `utf-8`.

```
FROM_VARBINARY(binary_expression, type)
```
### TO\_VARBINARY

Converts a string to its binary representation, useful for binary data handling. Supported encoding types: `hex`, `base64`, and `utf-8`.

```
TO_VARBINARY(string, type)
```
## JSON functions

### GET*JSON*OBJECT

Extracts a value from a JSON string using a JSONPath expression. Alias for `JSON_EXTRACT`.

```
GET_JSON_OBJECT(json_string, path)
```

```
SELECT GET_JSON_OBJECT('{"a": {"b": 1}}', '$.a.b') -- returns '1'
```
### JSON\_EXTRACT

Retrieves a specific value from a JSON string using a path expression, enabling JSON data manipulation

```
JSON_EXTRACT(json_string, json_path)
```
### JSON\_SERIALIZE

Converts a JSON value into its string representation, useful for storing or transmitting JSON data. `TO_JSON` is an alias for `JSON_SERIALIZE`. Both accept an optional options map, written using `MAP[...]` syntax. The Spark\-style `map('k', 'v')` function call form is rejected.

```
JSON_SERIALIZE(json_value)
JSON_SERIALIZE(json_value, options)
TO_JSON(json_value)
TO_JSON(json_value, options)
```
* `json_value` a struct, array, or map value
* `options` (optional) a map of literal key\-value pairs, written as `MAP['key1', 'value1', 'key2', 'value2']`. Supported keys: `dateFormat`, `timestampFormat`, `timeZone`, `locale`, `ignoreNullFields`, `pretty`.

```
SELECT TO_JSON(NAMED_STRUCT('ts', timestamp_col), MAP['timestampFormat', 'yyyy-MM-dd'])
-- returns '{"ts":"2026-08-15"}' when timestamp_col is 2026-08-15 12:34:56
```
## Map and struct functions

### MAP

Constructs a map from a list of alternating key/value pairs, using bracket literal syntax. The empty\-constructor form `MAP()` (parentheses, not brackets) is a separate special case, and produces an empty map typed as `Map<String, String>`.

```
MAP[key1, value1, key2, value2, ...]
MAP()
```
 Note With the CSV output format, the final output of a query cannot contain a `MAP` column. You can use map values anywhere else in the query. To output a map, index into it (for example `m['key']`) or wrap it in `TO_JSON()`.
```
SELECT TO_JSON(MAP()) -- returns '{}'
```
### STRUCT

Constructs a struct value from a list of expressions. Field names are always `col1`, `col2`, etc. — including when the expressions are column references.

```
STRUCT(expr1[, expr2, ...])
```
* `expr1, expr2, ...` one or more values to combine into a struct

```
SELECT TO_JSON(STRUCT(1, 'a')) -- returns '{"col1":1,"col2":"a"}'
```
### NAMED\_STRUCT

Constructs a struct value from alternating name/value pairs, with explicit field names.

```
NAMED_STRUCT(name1, value1[, name2, value2, ...])
```
* `name1, name2, ...` literal string field names
* `value1, value2, ...` values for each named field

```
SELECT NAMED_STRUCT('a', 1, 'b', 'x') -- returns a struct with field a = 1 and field b = 'x'
```
## Advanced functions

### CAST

`CAST` lets you convert a value or expression to a data type.

```
CAST(expression AS dataType)
```
### NAMED ROW

AMC supports the `NAMED_ROW()` function which helps group multiple columns under a single name.

```
SELECT NAMED_ROW('label1', <column1>, 'label2', <column2>) AS
<column3>
```
* \<label1\> and \<label2\> refer to labels to reference column1 and column2

## Statistical functions

### Standard deviation and variance

AMC provides support for several statistical functions that calculate the standard deviation and variance of either a population or of a sample set of data.

The functions `STDDEV_POP()` and `VAR_POP()` calculate the standard deviation and variance of the population, respectively. Use `STDDEV_POP()` and `VAR_POP()` when the values represent the entire population, and are not a sample.

The functions `STDDEV_SAMP()` and `STDDEV()` are synonyms for the same function. These functions can be used interchangeably because they calculate the standard deviation of a sample set of data, and provide the same results.

Similarly, the functions `VAR_SAMP()` and `VARIANCE()` are synonyms for the same function, and calculate the variance of a sample set of data. Use these functions when the values are a sample, and not for the entire population.

| Functions | Calculates | Population or Sample? |
| --- | --- | --- |
| STDDEV\_POP() | Standard deviation | Population |
| VAR\_POP() | Variance | Population |
| STDDEV\_SAMP() / STDDEV() | Standard deviation | Sample |
| VAR\_SAMP() / VARIANCE() | Variance | Sample |

#### STDDEV\_POP(), VAR\_POP()

```
STDDEV_POP(<values>)
VAR_POP(<values>)
```
* \<values\> A set of numeric values (integer, decimal, or floating\-point)

##### Query template

The query below calculates the standard deviation and variation of the clicks from the population of all clicks from cost\-per\-click (CPC) sponsored ads campaigns.

```
-- Instructional Query: How to use STDDEV_POP() and  VAR_POP() --

-- The population of clicks from CPC sponsored ads campaigns
WITH click_spend AS (
  SELECT
    -- spend is reported as microcents. Divide by 100,000,000 to get the cost in dollars/your currency.
    ad_product_type,
    spend / 100000000 AS spend
  FROM
    sponsored_ads_traffic
  WHERE
    clicks > 0
    and line_item_price_type = 'CPC'
)
SELECT
ad_product_type,
  STDDEV_POP(spend) AS STDDEV_POP_click_cost,
  VAR_POP(spend) as VAR_POP_click_cost
FROM
  click_spend
  group by 1
```
##### Example query results

| ad\_product\_type | stddev\_pop\_click\_cost | var\_pop\_click\_cost |
| --- | --- | --- |
| sponsored\_brands | 1\.55863 | 2\.42933 |
| sponsored\_products | 1\.15449 | 1\.33286 |

#### STDDEV(), VARIANCE()

```
STDDEV(<values>)
VARIANCE(<values>)
```
* \<values\> A set of numeric values (integer, decimal, or floating\-point)

##### Query template

The query below calculates the standard deviation and variance from a random sample of values for illustrative purpose.

```
-- Instructional Query: How to use STDDEV(), VARIANCE() --

-- Test data below is a sample of the population for illustrative purposes.
WITH test_data(test) AS (
  VALUES

    (20),
    (45),
    (30),
    (66),
    (50),
    (60),
    (85),
    (70)

)
SELECT
  STDDEV(test) as STDDEV_sample_stardard_deviation,
  VARIANCE(test) as VARIANCE_sample_variance

FROM
  test_data
```
##### Example query results

| stddev\_sample\_stardard\_deviation | variance\_sample\_variance |
| --- | --- |
| 21\.45261 | 460\.2142 |

#### STDDEV\_SAMP(), VAR\_SAMP()

```
STDDEV_SAMP(<values>)
VAR_SAMP(<values>)
```
* \<values\> A set of numeric values (integer, decimal, or floating\-point)

##### Query template

The query below calculates the standard deviation and variance from a random sample of clicks from cost\-per\-click (CPC) sponsored ads campaigns. Taking a random sample has the potential to result in better query performance, with statistically similar (but not exact) results from the population.

```
-- Instructional Query: How to use STDDEV_SAMP() and VAR_SAMP --

--10% random sample of clicks

WITH click_spend AS (
 SELECT
    -- spend is reported as microcents. Divide by 100,000,000 to get the cost in dollars/your currency.
    ad_product_type,
    spend / 100000000 AS spend
  FROM
    sponsored_ads_traffic
  WHERE
    clicks > 0
    and line_item_price_type = 'CPC'
    and random() <= 0.1
)

SELECT
ad_product_type,
  STDDEV_SAMP(spend) AS STDDEV_SAMP_click_cost,
  VAR_SAMP(spend) AS VAR_SAMP_click_cost
FROM
  click_spend
  group by 1
```
##### Example query results

Note that the sample standard deviation and variance results are slightly different from the population in the previous section.

| ad\_product\_type | stddev\_samp\_click\_cost | var\_samp\_click\_cost |
| --- | --- | --- |
| sponsored\_brands | 1\.55965 | 2\.43012 |
| sponsored\_products | 1\.15518 | 1\.33995 |

### SKEWNESS ()

The `SKEWNESS` function returns the estimate of the skewness of a set of numeric values (integer, decimal, or floating point). Skewness is a measure of the asymmetry of the distribution. The function will return one value per dimension.

**Skewed to the right**: A positive skewness value above 0\.5 indicates that the skew is positive, also known as ‘skewed to the right’ or ‘right tailed’; this means that most of the distribution is concentrated on the left, and the right tail is longer.

**Skewed to the left**: A negative skewness value below \-0\.5 indicates that the skew is negative, also known as ‘skewed to the left’ or ‘left tailed’; this means that most of the distribution is concentrated on the right, and the left tail is longer.

**Symmetrical**: A skewness value around 0 (between \-0\.5 \- 0\.5\) indicates that the distribution is nearly symmetrical on the left and the right. For example, a normal distribution has a skewness of zero.

```
SKEWNESS(<values>)
```
* \<values\> A set of numeric values (integer, decimal, or floating\-point)

##### Query template

```
-- Instructional Query: How to use SKEWNESS --

WITH click_spend AS (
    SELECT
    -- spend is reported as microcents. Divide by 100,000,000 to get the cost in dollars/your currency.
    ad_product_type,
    spend / 100000000 AS spend
  FROM
    sponsored_ads_traffic
  WHERE
    clicks > 0
    and line_item_price_type = 'CPC'
)
SELECT
        ad_product_type,
  SKEWNESS(spend) as SKEWNESS_click_cost
FROM
  click_spend
  group by 1
```
##### Example query results

The example results below for illustrative purposes show that both Sponsored Brands and Sponsored Products clicks are skewed to the right, or positively skewed. Sponsored Brands has a longer right tail, since its skewness value is about 35% larger than the value for Sponsored Products.

| ad\_product\_type | skewness\_click\_cost |
| --- | --- |
| sponsored\_brands | 3\.23764 |
| sponsored\_products | 2\.39026 |

### Percentile and Median

#### PERCENTILE(), APPROX\_PERCENTILE ()

The function `PERCENTILE()` calculates the value at a given percentile of a distribution of values. `APPROX_PERCENTILE()` calculates the approximate percentile of a distribution of values.

```
PERCENTILE(<values>, <percentile>)
APPROX_PERCENTILE(<values>, <percentile>)
```
* \<values\> A set of numeric values (integer, decimal, or floating\-point)
* \<percentile\> The percentile of the distribution to be found. Value must be between 0 and 1\.

#### MEDIAN()

The `MEDIAN()` function calculates the middle value of a set of numbers.

```
MEDIAN(<values>)
```
* \<values\> A set of numeric values (integer, decimal, or floating\-point)

##### Query template

```
-- Instructional Query: How to use PERCENTILE(), APPROX_PERCENTILE() and MEDIAN()--

WITH click_spend AS (
    SELECT
    -- spend is reported as microcents. Divide by 100,000,000 to get the cost in dollars/your currency.
    ad_product_type,
    spend / 100000000 AS spend
  FROM
    sponsored_ads_traffic
  WHERE
    clicks > 0
    and line_item_price_type = 'CPC'
)
SELECT
  ad_product_type,
  PERCENTILE(spend, .1) as PERCENTILE10_click_cost,
  PERCENTILE(spend, .9) as PERCENTILE90_click_cost,
  APPROX_PERCENTILE(spend, .1) as APPROX_PERCENTILE10_click_cost,
  APPROX_PERCENTILE(spend, .9) as APPROX_PERCENTILE90_click_cost,
  MEDIAN(spend) as MEDIAN_click_cost

FROM
  click_spend
  group by 1
```
##### Example query results

| ad\_product\_type | percentile10\_click\_cost | percentile90\_click\_cost | approx\_percentile10\_click\_cost | approx\_percentile90\_click\_cost | median\_click\_cost |
| --- | --- | --- | --- | --- | --- |
| sponsored\_products | 0\.18 | 2\.57 | 0\.18 | 2\.57 | 0\.81 |
| sponsored\_brands | 0\.37 | 3\.258 | 0\.37 | 3\.27 | 1\.09 |
