# Ads data manager and AMC | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/ads-data-manager-for-amc

# Ads data manager and AMC

Was this page helpful?Ads data manager lets you securely upload your first\-party data to Amazon Ads, through the Ads data manager console or the Ads data manager APIs, and share it across Amazon Ads products for planning, measurement and audiences. This page explains how Ads data manager relates to Amazon Marketing Cloud (AMC) and how to share Ads data manager data to AMC.

## How Ads data manager works with AMC

Ads data manager works in both advertiser and manager accounts. Upload your data once, through the Ads data manager console (no code required) or the Ads data manager APIs, and share it to multiple Amazon Ads destinations, including AMC. Sharing is done from a manager account. A dataset shared to AMC creates a queryable table in the "Advertiser uploaded" section of the Schema explorer.

## How sharing to AMC works

1. Upload or connect your first\-party data in Ads data manager, through the console or the Ads data manager APIs.
2. In Ads data manager, create an AMC destination for the dataset and select your linked AMC instance.
3. Ads data manager shares the dataset to the instance. The data appears in the "Advertiser uploaded" section of the Schema explorer.
4. Tables uploaded through Ads data manager include an `action` column, auto\-populated with the value `CREATE`.
5. Query the table in AMC like any other dataset.

## Prerequisites

* Your AMC instance is linked to the manager account that holds the data. Linking is a separate, one\-time step from sharing a dataset, and it is not self\-service today.

## Learn more

* [Ads data manager console overview](/API/docs/en-us/no-code-tools/adm/1_ads-data-manager-console-overview)
* [Ads data manager overview](/API/docs/en-us/guides/ads-data-manager/overview)
* [Ads data manager API reference](/API/docs/en-us/guides/ads-data-manager/api-and-events-reference)
* [Ads data manager destinations and data sharing](/API/docs/en-us/guides/ads-data-manager/destinations-and-data-sharing)
* [Advertiser data upload overview](/API/docs/en-us/guides/amazon-marketing-cloud/advertiser-data-upload/advertiser-data-overview)
* [Measure off\-Amazon conversions](/API/docs/en-us/guides/amazon-marketing-cloud/playbooks/off-amazon-conversions)
