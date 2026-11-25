# Overview - Amazon Marketing Cloud | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/overview

# Amazon Marketing Cloud

Was this page helpful?Amazon Marketing Cloud (AMC) is a secure, privacy\-safe, and cloud\-based clean room solution, in which partners and advertisers can structure custom queries to explore unique measurement questions, easily perform analytics across pseudonymized signals to address top business priorities, and build custom audiences ready for campaign deployment. AMC allows you to create reports over event\-level Amazon Ads inputs such as impressions and clicks from Amazon DSP ads, sponsored ads, and Amazon Live campaigns, as well as purchase events from Amazon stores. The instructions in the next few sections will assist you in making use of APIs to automate workflows, establish integrations, and develop tools and applications at scale.

 Important **The instance\-level APIs have been officially retired as on August 01, 2024\.** Use of the instance\-level APIs may result in `410` errors. To ensure uninterrupted operations, migrate to the AMC APIs on the Amazon Ads API as outlined in the [Migration guide](/API/docs/en-us/guides/amazon-marketing-cloud/amc-migration-hub/migration). To continue receiving query results in your connected S3 bucket, ensure that your **[connected AWS S3 bucket policy](/API/docs/en-us/guides/amazon-marketing-cloud/amc-migration-hub/migration-guide#updating-s3-bucket-policy-to-receive-query-results)** is updated. ## What are the benefits of AMC for advertisers?

With AMC, advertisers are able to more clearly answer measurement questions, gain further actionable insights, and build custom audiences ready for campaign activations. Some common use cases AMC can help you with are:

* Obtain more in\-depth findings about a particular campaign.
* Illustrate customer shopping journey in terms of media exposure, frequency, timing, etc.
* Understand the collective impact of media mix and isolate the incremental impact of a particular media usage.
* Assess how Amazon media contributes to sales at various Amazon store types and advertiser D2C channels.
* Look for correlation between engagement and audience attributes, and find your optimal audience segments.
* Assign credits to various touchpoints on the path\-to\-conversion of customers.
* Utilize ad engagement and conversion signals across channels and sources to build bespoke audiences for direct activation via Amazon DSP.
* Subscribe to Paid Features (beta) powered by Amazon Ads and third\-party providers to expand the scope and depth of insights.

 AMC education resourcesTo deepen your AMC knowledge, explore the [AMC education resources](https://learningconsole.amazonadvertising.com/student/path/37211-amazon-marketing-cloud-education?sid=da9d26fa-93a7-4e15-8fbb-20c519d58d8b&sid_i=3) available on Amazon Ads learning console.## Key features

Advertisers and partners can now access Amazon Marketing Cloud APIs from the Amazon Ads [advanced tools center](/API/docs/en-us/guides/overview), along with APIs for other Amazon Ads solutions such as sponsored ads and Amazon DSP. As the rest of Amazon Ads APIs, these new AMC APIs follow the industry\-standard OAuth 2\.0 authorization framework and use a consistent base URL to gain access to AMC resources.

The new AMC APIs currently support features including reporting, signal management, and advertiser audience management.

The migration of the AMC APIs to Amazon Ads API offers further enhanced security, usability, and performance, allowing developers to easily utilize, manage, and build with these APIs. Specifically,

* Developers can now use the same authorization and authentication mechanism as rest of the Amazon Ads solution APIs, via client applications administered by Login with Amazon. **This streamlines and simplifies the set up and access to relevant AMC accounts and instances.**
* Multiple users and partner organizations can now access one AMC instance at the same time. This enables more scalable AMC usage and operations, and it is especially beneficial for partners handling multiple AMC instances across advertisers.
* Developers can now find AMC APIs grouped by functional categories, and following a standard endpoint naming convention composed of base URL, API path, and resources. **This helps developers to easily comprehend and identify the APIs to use.**

## Where is AMC available?

* **North America:** United States, Canada, Mexico
* **South America:** Brazil
* **Europe:** Germany, Spain, France, Italy, Netherlands, United Kingdom, Sweden, Turkey, Poland, Belgium, Ireland
* **Middle East:** Saudi Arabia, United Arab Emirates, Egypt
* **Asia Pacific:** Australia, India, Japan, Singapore
* **Africa:** South Africa, Nigeria
