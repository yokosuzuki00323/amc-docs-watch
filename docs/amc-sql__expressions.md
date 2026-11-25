# Amazon Marketing Cloud SQL expressions | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/amc-sql/expressions

# Supported expressions

Was this page helpful?## CONTAINED IN

The `CONTAINED IN` function returns true if the result of the input expression is equal to any of the expressions that follow the input expressions. If no match is found, the function returns `FALSE`.

```
CONTAINED_IN(testExpression, expression [, expression]*)
```
## BUILT\-IN PARAMETER

This function returns a built\-in parameter by name.

```
BUILT_IN_PARAMETER('parameterName')
```
 Note Currently AMC supports `TIME_WINDOW_START` and `TIME_WINDOW_END`. Both return the start or end of the overall workflow time window.## CUSTOM PARAMETER

Return input parameter value by name set at the workflow definition level.

```
CUSTOM_PARAMETER('parameterName')
```
## UUID

Return random universally unique identifier (UUID) string.

```
UUID()
```
