# Amazon Marketing Cloud - AWS Clean Rooms | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/acr/8_query

# Query data in your collaboration instances

Was this page helpful?After you have uploaded your data in your collaboration instances, and the data appears under the AMC Console **Schema explorer** under **Advertiser connected** of the **Query editor** page, you can begin to query data.

You can query your data either through the [AMC Console](/API/docs/en-us/guides/amazon-marketing-cloud/acr/8_query#query-data-using-the-amc-console) or programmatically using [AMC APIs.](/API/docs/en-us/guides/amazon-marketing-cloud/acr/8_query#query-data-using-amc-apis)

## Query data using the AMC console

Before running queries in the AMC console, review the [limitations](/API/docs/en-us/guides/amazon-marketing-cloud/acr/limitations) of the AMC console and specifications on using the date range for handling queries.

To run queries using the AMC console, access the AMC console. Notice that the console:

* Displays the status of your collaboration instance as `Active` on the **Instance info** page.
* Displays your uploaded data in the **Schema explorer** under **Advertiser connected** on the **Query editor** page.
* Displays the name of the **collaboration instance** in the **Instance** drop\-down.
* Displays a notification above the **Query editor** indicating that the instance uses AWS Clean Rooms collaboration.

You and users from your organization can write queries in the AMC **Query editor** using your uploaded data or data in your collaboration instance.
After the query runs, the results are available on AWS Clean Rooms console.
Access the AWS Clean Rooms console.
If you are the result receiver (you have a service role to receive results), you can:

* [View, copy, or download the query results](https://docs.aws.amazon.com/clean-rooms/latest/userguide/receive-query-results.html) on the **Results** section of the **Queries** tab.
* View and download the query results from Amazon S3 on the **Query results settings defaults** of the **Queries** tab.

## Query data using AMC APIs

The AMC APIs that are supported for collaboration instances listed below are categorized broadly by the following core functions:

* [Administration resources](/API/docs/en-us/amc-administration)
* [Advertiser data upload resources](/API/docs/en-us/amc-advertiser-data-upload)
* [Workflow management services resources](/API/docs/en-us/amc-reporting)

To make your API calls, you will need to know the following:

* [Base URL](/API/docs/en-us/guides/amazon-marketing-cloud/get-started/make-your-first-call#ads-api-base-urls)
* [Marketplace identifiers](/API/docs/en-us/guides/amazon-marketing-cloud/get-started/make-your-first-call#marketplace)
* [Header parameters](/API/docs/en-us/guides/amazon-marketing-cloud/get-started/make-your-first-call#header-parameters)
