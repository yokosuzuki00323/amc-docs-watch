# How does Amazon Marketing Cloud work | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/how-amc-works

# How AMC works

Was this page helpful?Pseudonymized inputs from Amazon Ads campaign events such as ad impressions, ad clicks, and ad\-attributed conversions that span across media, including streaming TV, audio, video, display, and sponsored ads are uploaded into AMC instances. Examples of common signal types that are uploaded include direct\-to\-consumer (D2C) store sales information, CRM records, and product catalog mapping.

 Did you know?AMC prioritizes privacy and security by design by accepting only pseudonymized information. All information in your AMC instance is handled in strict accordance with the Amazon privacy notice, and raw event information cannot be exported.The signals you choose to upload stay within your dedicated AMC instance, and cannot be accessed or exported by Amazon.

 Note To be joined with Amazon Ads signals, your signals need to contain joinable fields such as pseudonymized email addresses, and phone numbers, or product `ASIN`s. For details on [joining fields](/API/docs/en-us/guides/amazon-marketing-cloud/amc-sql/basics#join), see [AMC SQL reference](/API/docs/en-us/guides/amazon-marketing-cloud/amc-sql/overview).Through AMC, you may want to analyze the journey and path to conversion of your audience, or audience penetration, or want to consider the frequency distribution of an ad or optimal frequency that leads to a conversion.

All analysis takes place within AMC, across dimensions like audiences, device, time, or campaigns to name a few and results are aggregated to generate anonymous reports that you can export.

 AMC education resourcesTo deepen your AMC knowledge, explore the [AMC education resources](https://learningconsole.amazonadvertising.com/student/path/37211-amazon-marketing-cloud-education?sid=da9d26fa-93a7-4e15-8fbb-20c519d58d8b&sid_i=3) available on Amazon Ads learning console.## AMC UI and APIs

Amazon Marketing Cloud (AMC) is accessible through two primary methods:

* Access via the web\-based user interface within Amazon Ads console
* Programmatic integration through the Amazon Ads API

Please note that the AMC user interface is currently available exclusively in English, with no localization options for other languages.

## Gain access to AMC

AMC supports two access models:

**Self\-service access (a single advertiser per instance).** If you have a sponsored ads account or a [global advertising account](https://advertising.amazon.com/help/GXKXR56ZCMJ3WCS4), you can use AMC self\-service access to automatically create an AMC instance for that account and start using AMC within minutes. Each account gets a single instance scoped to that one advertiser; you cannot add other advertisers to it.

* Access AMC through the user interface by navigating to AMC within your Amazon Ads console, or, after you onboard to the Amazon Ads API, follow the instructions in [Instant self\-service access to AMC](/API/docs/en-us/guides/amazon-marketing-cloud/get-started/instant-access-to-amc).

**Account\-based access (multiple instances and advertisers).** If you want an instance whose scope includes multiple advertisers or Amazon DSP advertisers, use an account that supports multiple instances:

* **[Manager accounts](https://advertising.amazon.com/help/GU3YDB26FR7XT3C8)** are the self\-service option. A manager account can own multiple AMC instances, and each instance can include multiple advertisers linked to the manager account. For details, see [AMC administration functions](/API/docs/en-us/guides/amazon-marketing-cloud/admin/1_amc_administration).
* **AMC accounts** are provisioned by your AdTech AE or Partner when you apply for access. Your account is managed by a user your organization designates as the "AMC admin", who can create instances, add advertiser IDs to instances, and add users to view and analyze data in the assigned instances. For details, see [AMC administration functions](/API/docs/en-us/guides/amazon-marketing-cloud/admin/1_amc_administration).

## AMC accounts and instances

To use AMC, you must first understand AMC account and instances, the fundamental building blocks of AMC that allow for a hierarchical structure.
An [AMC account](/API/docs/en-us/guides/amazon-marketing-cloud/how-amc-works#amc-accounts) represents the advertiser or agency as the top\-level organizational unit, and contains one or more [instance(s)](/API/docs/en-us/guides/amazon-marketing-cloud/how-amc-works#amc-instances). An instance is the actual AMC "clean room" that is set up for a given advertiser or company.

### AMC accounts

Access to AMC is managed at the account level. An admin user can create instances, grant organization users access to specific instances within the account, and invite additional admins. This granular access control allows selective user access to accounts and instances, enabling agencies to manage multiple accounts across multiple advertisers, brands, or entities under a single corporate umbrella.

 Note For self\-service instances created using the instant access API, the account ID is the advertiser's own account ID — the sponsored ads entity ID for a sponsored ads account, or the global advertising account ID (beginning with `amzn1.ads-account.g.`) for a global advertising account.For details see [AMC account management](/API/docs/en-us/guides/amazon-marketing-cloud/admin/account-management).

### AMC instances

An instance contains records from only a single brand or company. AMC allows for the following types of instances:

* **Standard instances**: Contains Amazon Ads events for a single advertiser, and mapped to one or multiple Amazon DSP accounts and or sponsored ads entities. Admin users can [create standard instances](/API/docs/en-us/guides/amazon-marketing-cloud/admin/instance-management#create-an-instance).
* **Sandbox instances**: Contains synthetic signals generated to mimic the structure and statistical properties of AMC signals. All AMC accounts have been granted a [sandbox instance](/API/docs/en-us/guides/amazon-marketing-cloud/amc-sandbox). This type of instance is not supported for AMC instances created using the instant access API.
* **Collaboration instances**: The integration of [AMC on AWS Clean Rooms](/API/docs/en-us/guides/amazon-marketing-cloud/acr/1_overview) enables advertisers to seamlessly collaborate with Amazon Ads exclusive signals, using your data from the AWS environment of the advertiser. Reach out to your AdTech AE to request a collaboration instance. This type of instance is not supported for AMC instances created using the instant access API.

 Note Unless otherwise specified, all references are to standard AMC instances.
Admin users can create standard instances. For more details, see [Create instances](/API/docs/en-us/guides/amazon-marketing-cloud/admin/instance-management#create-an-instance).### Data in your AMC instance

Data in your instance can be Amazon owned or customer or advertiser owned.

Data from your Amazon Ads campaign events can include impressions and clicks from Amazon DSP ads and Amazon sponsored ads campaigns, as well as purchase events from Amazon stores to perform advanced analytics.

After your instance is set up, it is back\-filled with Amazon\-owned advertising insights (if available) from your DSP or sponsored ads accounts. By default, advertising events accumulate the most recent event\-level information, ranging from up to 13 months to 5 years (for eligible traffic data views). Retention varies by data view; refer to [AMC data retention](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/data-retention).

You can also bring in your own customizable datasets to AMC instances by sharing data from [Ads data manager](/API/docs/en-us/no-code-tools/adm/1_ads-data-manager-console-overview) (recommended) or by uploading with [Advertiser data upload](/API/docs/en-us/guides/amazon-marketing-cloud/advertiser-data-upload/advertiser-data-overview). The datasets containing supported identifiers can be joined with AMC data to attribute off\-Amazon events (purchases, sign\-ups, store visits, etc.) to Amazon advertising events such as impressions and clicks.
You can then leverage both signals from your Amazon campaigns and your uploaded datasets for planning and measurement use cases to gain insights, optimize campaigns, and finally create audiences.

You can also opt\-in for AMC **Paid features** to avail more datasets and insights for deeper analysis of your campaigns and audience creation outcomes.

 Important Any data you choose to upload stay within your dedicated AMC instance, and cannot be accessed or exported by Amazon.For details, see [AMC data sources](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/overview) and review the [important notes for querying the data sources](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/overview#important-notes-for-querying-data-sets).

### Queries in AMC

AMC allows you to access the data from your instances through the use of queries written in **AMC Structured Query Language (AMC\-SQL)**. Queries can be written to generate custom metrics and insights tailored to your business, enabling you to make more informed decisions on your campaign spend.

AMC SQL is a custom query language that supports most of the basic SQL operations, designed to help advertisers interact with event\-level records to generate aggregated outputs, which lead to insights for campaign measurement, audience analysis, media optimization, or to create audiences.

 Important While you can perform queries within each instance, you cannot perform queries across instances.When you submit a query for processing, the AMC [data aggregation thresholds](/API/docs/en-us/guides/amazon-marketing-cloud/aggregation-threshold) are enforced to ensure the output contains aggregated and anonymous results to protect customer privacy.

You can use the AMC [workflow management service](/API/docs/en-us/guides/amazon-marketing-cloud/reporting/create-workflow) to programmatically manage your queries.

After you run your queries, you [can get your results](/API/docs/en-us/guides/amazon-marketing-cloud/reporting/get-your-results) in any of the following ways:

* [Through a download URL.](/API/docs/en-us/guides/amazon-marketing-cloud/reporting/get-your-results#download-your-query-results)
* [Through your connected S3 bucket, to which your query results are stored.](/API/docs/en-us/guides/amazon-marketing-cloud/reporting/get-your-results#view-your-workflow-output-in-the-amazon-s3-bucket)

 Note To send the results of your queries to your S3 bucket, you will need to [define an S3 bucket](/API/docs/en-us/guides/amazon-marketing-cloud/get-started/get-started#set-up-s3-buckets-optional).
