# Amazon Marketing Cloud - AWS Clean Rooms | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/acr/6_upload_event

# Bring event data into the collaboration instance

Was this page helpful?After you have created a membership and joined the collaboration in AWS Clean Rooms, you can bring your event data to the collaboration instance from any commercial and opt\-in regions that are supported by AWS Glue. For a list of Glue\-supported regions for both commercial and opt\-in, refer to the [regions in the Service Endpoints section](https://docs.aws.amazon.com/general/latest/gr/glue.html).

 Note Event table headers and data can contain underscores and must essentially have a column titled `customer_user_id` in order to join with identity data.To bring your event data to the collaboration, perform the following steps:

1. [Prepare your data tables](https://docs.aws.amazon.com/clean-rooms/latest/userguide/prepare-data.html) for queries. When preparing your data tables, take note of the [prerequisites](https://docs.aws.amazon.com/clean-rooms/latest/userguide/prepare-data.html#prep-data-tables-prereq) and know that the *Amazon S3 bucket cannot be registered with AWS Lake Formation*.

 Important Ensure that the S3 location for receiving the query results is a different location from the bucket containing the event data that you bring into the collaboration.3. [Create a configured table to be used within a collaboration](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-configured-table.html) through your AWS Clean Rooms console or use the [CreateConfiguredTable](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateConfiguredTable.html) API.
4. [Configure analysis rules](https://docs.aws.amazon.com/clean-rooms/latest/userguide/configure-analysis-rule.html) to your configured tables. ([CreateConfiguredTableAnalysisRule](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateConfiguredTableAnalysisRule.html)).

Use the following AMC custom analysis rule to set up your data source:

```
"allowedAnalyses": [ "ANY_QUERY" ],
"allowedAnalysisProviders": [ "657425294073", "813176346477" ],
"additionalAnalyses": "ALLOWED"
```
 Note An analysis rule determines how the configured table can be analyzed. If you want to set up your data source to allow for creating audiences, you must set `additionalAnalyses` to `ALLOWED`. If your business does not require creating audiences from your data source, set the parameter to `NOT_ALLOWED`.4. [Associate the configured table](https://docs.aws.amazon.com/clean-rooms/latest/userguide/associate-configured-table.html) with the collaboration instance using ([CreateConfiguredTableAssociation](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateConfiguredTableAssociation.html)).

 Important Use the custom trust policy role you created to read data in section [Access to AWS](/API/docs/en-us/guides/amazon-marketing-cloud/acr/3_setup_requirements#access-to-aws).
5. Create collaboration analysis rules, depending on your use case. To allow both measurement and audience queries, navigate to your collaboration instance in the AWS Clean Rooms console.

	* Access **Tables**\>**Tables associated by you** and
	* Click **Not Ready** under the **Direct analysis status** column. The **Not ready for direct analysis** popup appears.
	* Click **Configure**, and in the page that appears, scroll to the **Results delivery** – **Members allowed to receive results for query output**, select **both members ('Internal results receiver' and 'Advertiser – you'**). If you do not want to create audiences using your data source, then select only the 'Advertiser – you' for results delivery.
6. Go back to the AMC console to view the data in the **Advertiser Connected** section of the Schema Explorer.
