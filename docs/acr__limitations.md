# Amazon Marketing Cloud - Account Management | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/acr/limitations

# AMC–AWS Clean Rooms limitations

Was this page helpful?The following list summarizes AMC\-AWS Clean Rooms limitations:

## Query handling

When writing queries using collaboration data, the **AMC Query editor \- date range** options are not supported.

* For querying over time ranges, make sure your data contains a time stamp column.
* Define the date range as part of the query.
* To restrict the date range in queries using advertiser connected data, use

```
  WHERE maineventtimecolumn >= BUILT_IN_PARAMETER('TIME_WINDOW_START')
  AND maineventtimecolumn < BUILT_IN_PARAMETER('TIME_WINDOW_END').
```
 Note `mainEventTimeColumn` is the event time column on which the date range filter should apply.Collaboration instances cannot query synthetic data.

## Query results

All results of your queries will go directly to the Amazon S3 bucket associated with your collaboration instance that you specified when creating a membership to join the collaboration.
Query results can be retrieved for queries run within the previous 90 days. To access results of queries executed prior to this 90\-day period, re\-execute those queries.

## APIs

Schedules and workflow executions will not throw errors if you make an API call prior to accepting the collaboration invite.
