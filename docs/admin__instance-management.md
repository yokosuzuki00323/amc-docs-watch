# Instance management | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/admin/instance-management

# Instance management

Was this page helpful?An AMC instance is the actual cloud\-based clean room that is set up for a given advertiser or company in which event\-level signals for the given set of advertiser Ids start to accumulate. The signals in instances are made available for querying to generate analytics and build audiences. Some advertisers have multiple instances to represent different business units, brands, or subsidiaries, but as long as those instances all represent the same company advertising on Amazon they can be within one instance created under a single account.

Admin users can create instances and then add the identifiers of the advertisers (whether sponsored ads or Amazon DSP) to include in the instance.

 Note While you can perform queries within each instance, you cannot perform queries across instances.The day an instance is created, it is back\-filled with advertising insights, and will accumulate signals up to 13 months to 5 years, depending on the data view. This means that as time goes on, you will always have the most recent 13 months to 5 years of event\-level information in the instance. Retention varies by data view; refer to [AMC data retention](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/data-retention).

* Instances will contain the most recent 13 months to 5 years of records, depending on the data view, with older records having aged out.
* Before running queries, note that AMC does not ingest data at real\-time and propagates your ad activity data after a time\-lag. As a best practice, AMC recommends that you select a date range of 48\-hours prior to the current date.
* An [S3 bucket associated with your instance](/API/docs/en-us/guides/amazon-marketing-cloud/get-started/get-started#set-up-s3-buckets-optional) is an optional requirement. When your instance is created, admin user can set up an S3 bucket to which the instance will write results.

## Create an instance

AMC now offers **admin users** the ability to create instances.
Use the `POST` operation of the `/amc/instances` endpoint to create an instance with the instance name as the only mandatory request parameter. The mandatory header parameters are listed below:

| Header | Description |
| --- | --- |
| `Amazon-Advertising-API-ClientId` | The client Id related to a Login with Amazon application. |
| `Amazon-Advertising-API-MarketplaceId` | The marketplace identifier for the [marketplace](/API/docs/en-us/guides/amazon-marketing-cloud/get-started/make-your-first-call#marketplace). |
| `Amazon-Advertising-API-AdvertiserId` | The AMC account identifier. See [Retrieve accounts](/API/docs/en-us/guides/amazon-marketing-cloud/admin/account-management). |
| Authorization | Login with Amazon token in the form of `Bearer {token}`. |

### Sample request

```
{
   "instanceName": "sampleinstance"
}
```
The following optional parameters can be passed as the request body:

* `advertiserName:` Optionally, pass the name of the advertiser (`advertiserName`) associated with the instance you are creating, ensure that the advertiser name can only contain letters (both uppercase and lowercase), numbers, and spaces. Special characters (except spaces) are not allowed in the advertiser name, and the advertiser name cannot start or end with a space.
* `awsAccountId`: If required, and if you are using a connected Amazon Web Service (AWS) account in which you will create an Amazon S3 bucket to receive your query results, you can specify the `awsAccountId` of connected AWS account.
* `s3BucketName`: If you have already created an Amazon S3 bucket, you can also optionally pass the Amazon S3 (`s3BucketName`) bucket name to which the results of the queries run in this instance will be saved.

Following is a sample request body with all the optional parameters included:

```
{
   "instanceName": "myinstance",
   "advertiserName": "Advertiser-A",
   "awsAccountId": "682015411111",
   "s3BucketName": "my-S3-Bucket"
}
```
AMC will validate your request and respond as shown below.

### Sample response

```
{
    "instance": {
        "instanceId": "amc1alal2aa",
        "instanceName": "myinstance",
        "instanceType": "STANDARD",
        "customerCanonicalName": "Advertiser-A",
        "creationStatus": "REQUESTED",
        "creationDatetime": null,
        "s3BucketName": "my-S3-Bucket",
        "awsAccountId": "682015411111",
        "entities": [
            "NA"
        ],
        "dataUploadAwsAccountId": "811639200111",
        "apiEndpoint": null,
        "acrCollaboration": null,
        "optionalDatasets": [],
        "advertiserTypes": []
    }
}
```
The operation initiates a request to create a standard instance.

 Note Your `advertiserName` is logged in the `customerCanonicalName` parameter of the response body. In case you need to modify the `advertiserName`, copy the value displayed in the `customerCanonicalName` parameter and use the `PUT /amc/instances/{instanceId}` endpoint to make the change.The instance request process goes through the following statuses until the request succeeds and an instance is ready:

* `REQUESTED`: Instance creation is successfully requested.
* `SUBMITTED`: Instance creation request is submitted for processing.
* `IN_PROGRESS`: Instance creation is in progress.
* `SUCCEEDED`: This field is no longer in use, and is replaced with the `COMPLETED` status.
* `COMPLETED`: Instance creation is successful.

 Note Instances created through this API are empty shells without advertiser data. Administrators can create up to 8,000 instances per AMC account using this API, with no restrictions on the number created daily.### View instance details

To view the details or the status of a specific instance, use the `GET /amc/instances/{instanceId}` endpoint.

 Note After an instance is created, you can create an [advertisers/updates](/API/docs/en-us/guides/amazon-marketing-cloud/admin/instance-management#add-or-remove-advertisers) request to instance to include advertisers to the instance.To view all instance details associated with your account, use `GET /amc/instances`.

 Note You can also view all instance details from the AMC console, including which Amazon DSP and sponsored ads advertisers are associated with the instance, the connected S3 bucket name, and the AWS account ID. From the AMC console, go to the **Instance** tab drop\-down at the top\-right corner of the page and click **Instance info** to access the Instance info page.The response displays the following fields, that can be edited using the `PUT/amc/instances/{instanceId}`:

* + `instanceName`: The name of the instance
	+ `customerCanonicalName`: This is the same as the `advertiserName` .
	+ `awsAccountId`: The AWS account connected to the instance.
	+ `s3BucketName`: The S3 bucket connected to the instance.
	+ `advertiserTypes`: Indicates if it is an Amazon DSP account or sponsored ads account.
* The other fields are internal\-only and have set expected values.
	+ `apiEndpoint`: The base URL for the instance/account.
	+ `entities`: \["NA"] \- NA will always be the value for this field.
	+ `acrCollaboration`: Details for AWS Clean Room backed instance.
	+ `dataUploadAwsAccountId`
		- The AWS account ID by Amazon for each AMC instance. It allows AMC users to grant an AMC instance permission to read data files from an S3 bucket(s).

## Update instance information

To update an instance, use `PUT/amc/instances/{instanceId}`. You can request modifications only after the status of the instance is `COMPLETED`. You can modify values for the following parameters:

* `instanceName`
* `advertiserName`
* `awsAccountId`
* `s3BucketName`

### Update connected AWS account

 Important The `POST/amc/instances/{instanceId}/updateCustomerAwsAccount` endpoint is flagged for deprecation. Use `PUT/amc/instances/{instanceId}` instead to update your connected AWS account.The `POST/amc/instances/{instanceId}/updateCustomerAwsAccount` operation allows you to manage the AWS account associated with your instance. Results (from both manual queries run in the UI and automated queries scheduled through APIs) are delivered to the S3 bucket associated with your AWS account. The `updateCustomerAwsAccount` operation accepts the `awsAccountId` and the S3 bucket name as the payload of the request body and returns a CloudFormation link that you can use to update the S3 bucket.

#### Sample request

```
{
  "awsAccountId": "811111100111",
  "bucketName": "My-S3-bucket"
}
```
#### Sample response

```
{
    "cfnBucketUrl": "https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://public-file-hosting-repository.s3.amazonaws.com/cfn-template.yaml&stackName=amcDeliveryBucketStack&param_pBucketName=My-S3-bucket&param_pCrossAccountAccessAccountId=811111100111"
}
```
### Delete an instance

To delete a specific instance, use `DELETE/amc/instances/{instanceId}`. The requested instance is deleted only if the `creationStatus` of the requested instance is `SUCCEEDED`.

 Important The delete action cannot be undone and you will lose all data stored in the instance. When deleting instances, proceed with caution.## Add or remove advertisers

After successfully creating your instance, you can add the IDs of the advertiser accounts you want to include in your instance using the `POST /amc/instances/{instanceId}/advertisers/updates` endpoint.

While all instances start with the same standard configuration, the type of advertisers you add to your instance determines its classification as a sponsored ads or an Amazon DSP instance. AMC also allows for a hybrid instance, which contains both sponsored ads and Amazon DSP advertisers.

### Add a single advertiser to an instance

Depending on the type of advertiser you add (Amazon DSP advertiser or sponsored ads advertiser), the request body is constructed as illustrated below:

| Request body parameter | Amazon DSP advertisers | Sponsored ads advertiser |
| --- | --- | --- |
| `advertiserType` | `DISPLAY` | `SPONSORED_ADS` |
| `id` | Numerical ID, retrieved using [GET /dsp/advertisers](/API/docs/en-us/dsp-advertiser). Copy the value of the `advertiserId` returned in the response body. | ID prefixed with `ENTITY`, retrieved using [POST /adsAccounts/list](/API/docs/en-us/account-management#/Account/ListAdsAccounts). Copy the value of the `entityId` parameter in the response body. |
| `marketplaceId` | Not required for Amazon DSP advertisers. | Required for sponsored ads account. Use the [marketplace ID](/API/docs/en-us/guides/amazon-marketing-cloud/get-started/make-your-first-call#marketplace) tied to the country of your sponsored ads account. Note that this `marketplaceId` may differ from the `marketplaceId` of your AMC account. |

**Sample request \- sponsored ads**

```
{
  "advertisersToAdd": [
      {
        "id": "ENTITY1X1X1XX1X1117",
        "type":"SPONSORED_ADS",
        "marketplaceId":"ATVPDKIKX0DER"
      }
  ],
  "advertisersToRemove": [
  ]
}
```
**Sample response \- sponsored ads**

```
{
    "advertiserUpdate": {
        "updateId": 1,
        "status": "PENDING",
        "advertisersToAdd": [
            {
                "id": "ENTITY1X1X1XX1X1117",
                "marketplaceId": "ATVPDKIKX0DER",
                "type": "SPONSORED_ADS"
            }
        ],
        "advertisersToRemove": []
    }
}
```
**Sample request \- Amazon DSP**

```
{
  "advertisersToAdd": [
      {
        "id": "9998887770000",
        "type":"DISPLAY"
      }
  ],
}
```
**Sample response \- Amazon DSP**

```
{
    "advertiserUpdate": {
        "updateId": 1,
        "status": "PENDING",
        "advertisersToAdd": [
            {
                "id": "9998887770000",
                "marketplaceId": NULL,
                "type": "DISPLAY"
            }
        ],
        "advertisersToRemove": []
    }
}
```
The request creates an advertiser update for the requested AMC instance to add (or remove) advertiser ids to the instance.

 Note If you are adding advertisers to your instance for the first time, you may omit the `advertisersToRemove` section from your request body. You may use it in a subsequent call.#### Single advertiser addition approval

AMC now automatically approves advertiser additions for single advertiser requests. When an admin user requests to add a single advertiser to any instance type, AMC verifies that the advertiser's data can be accessed for the instance's account.

 Note How this access is verified **branches by the account type that owns the instance**:
 *For* *AMC account* *instances, AMC verifies the access of the* *requesting admin user* *to the advertiser's data (the [admin user access verification](/API/docs/en-us/guides/amazon-marketing-cloud/admin/instance-management#admin-user-access-verification-amc-accounts) below).* For **manager account** instances, AMC instead verifies that the advertiser is **linked to the manager account** (see [Manager account instances](/API/docs/en-us/guides/amazon-marketing-cloud/admin/instance-management#manager-account-instances) below). The requesting user must be a manager account admin.In both cases, when you combine multiple advertisers in one instance, the advertisers must belong to the same brand or parent company. Being linked to the same manager account does not by itself establish a brand relationship. For more information on managing brands, see [Amazon Brand Registry for advertising](https://advertising.amazon.com/help/GKXEAMWZVR99QV37) and [Manage your brand and products](https://advertising.amazon.com/help/GVEZ2EQ2CQZC7WUL).##### Admin user access verification (AMC accounts)

For **AMC account** instances, AMC verifies the access of the requesting admin user to the advertiser account through one of the following methods:

| Advertiser Type | Admin User Verification |
| --- | --- |
| **Amazon DSP** | **Direct console access**AMC verifies if the requesting admin user has direct access to the account of the advertiser through the Amazon Ads console. You can also validate your direct access using [Advertising User Permissions Management APIs.](/API/docs/en-us/user-permissions)If the verification is successful, the requested advertiser ID is immediately added to the instance with access to historical data (13 months to 5 years, depending on the data view). |
| **Sponsored ads** | **Direct console access**AMC verifies if the requesting admin user has direct access to the account of the advertiser through the Amazon Ads console. You can also validate your access using [Advertising User Permissions Management APIs.](/API/docs/en-us/user-permissions)or **Indirect API\-only access**:\- The requesting admin user has been granted access to the data of the advertiser through a Login with Amazon (LwA) authorization. **Indirect API\-only access only applies to partner accounts. The LwA application that was granted access must be linked to the partner account and the requesting AMC admin user invoking the API must be a user in the partner account**. \- The initial relationship of the requesting admin user with the advertiser data is established by making API calls. This can be done either through one campaign management call or two calls of any other type. Note that after making the initial API calls, there is a mandatory 3\-day waiting period. This time allows AMC to establish and verify the connection between the LwA client ID of the requesting admin user and the advertiser account. **Note that to ensure the authorization relationship is current and active, the initial API call must have been made within the last 90 days.**\- Submit your request to add the advertiser using the `POST/amc/instances/{instanceId}/advertisers/updates` endpoint. Ensure that this call is made 3 days after the mandatory wait period. Once verified, the requested advertiser ID is immediately added to the instance with access to historical data (13 months to 5 years, depending on the data view). If the access of the requesting admin user to the data of the advertiser cannot be verified, the following error message is returned, and the request is rejected. `This request was rejected because the requesting user does not have access to the following advertisers included in the request: ${advertisers}. You can resolve this by gaining direct access to the advertiser account(s) via the Amazon Ads console, or access to the advertiser data through a Login with Amazon (LwA) authorization and make at least one API call within the past 90 days before making this request again.`For more information on LwA access, see [Add users to your organization's developer account](https://developer.amazon.com/docs/app-submission/manage-account-and-permissions.html#add_other_users). |

##### Manager account instances

For **manager account** instances, AMC does not verify the requesting user's individual access to each advertiser. Instead, access is determined by whether the advertiser account is **linked to the manager account**. The requesting user must be an administrator of the manager account.

The type of link required depends on the advertiser type:

* **Sponsored ads advertisers**: any link between the sponsored ads account and the manager account is sufficient to add the advertiser to the manager account's instances.
* **Amazon DSP advertisers**: an **admin link** is required. This admin link exists only between a DSP account (CFID) and the manager account that created that DSP account.

 Important The DSP admin link is not transferable and cannot be recreated. If a DSP advertiser was created under a different manager account, or was not created under a manager account, you cannot add it to this manager account's instances. To add a DSP advertiser to a manager account instance, the DSP account must have been created under that same manager account.The same\-brand requirement still applies: advertisers combined in a single manager account instance must belong to the same brand or parent company, and requests that cannot be confirmed programmatically follow the same review and rejection behavior described above.

**Keeping advertisers accessible.** AMC continuously verifies that every advertiser attached to a manager account instance is still accessible through the manager account. If an advertiser account is later unlinked from the manager account, AMC blocks the instance from further use until you resolve the issue. To restore access, either remove the affected advertiser from the instance, or re\-link the advertiser account to the manager account.

 Important In case a previous modification request is in progress (status\=`PENDING` or `UPDATING`), the new update request will fail.### Add multiple advertisers to an instance

You can add up to 10 advertiser Ids to an instance in a single modification call. However, an instance is limited to 2,000 advertiser Ids in total.

**Sample request \- sponsored ads**

```
{
  "advertisersToAdd": [
      {
        "id": "ENTITY1X1X1XX1X1117",
        "type":"SPONSORED_ADS",
        "marketplaceId":"ATVPDKIKX0DER"
      },
      {
        "id": "ENTITY1X1X1XX1X1118",
        "type":"SPONSORED_ADS",
        "marketplaceId":"ATVPDKIKX0DER"
      }
  ],
  "advertisersToRemove": [
  ]
}
```
**Sample response \- sponsored ads**

```
{
    "advertiserUpdate": {
        "updateId": 1,
        "status": "PENDING",
        "advertisersToAdd": [
            {
                "id": "ENTITY1X1X1XX1X1117",
                "marketplaceId": "ATVPDKIKX0DER",
                "type": "SPONSORED_ADS"
            }
            {
                "id": "ENTITY1X1X1XX1X1118",
                "marketplaceId": "ATVPDKIKX0DER",
                "type": "SPONSORED_ADS"
            },
        ],
        "advertisersToRemove": []
    }
}
```
**Sample request \- Amazon DSP**

```
{
  "advertisersToAdd": [
    {
        "id": "9998887770000",
        "type":"DISPLAY"
    }
    {
        "id": "9998887770001",
        "type":"DISPLAY"
    },
  ],
}
```
**Sample response \- Amazon DSP**

```
{
    "advertiserUpdate": {
        "updateId": 1,
        "status": "PENDING",
        "advertisersToAdd": [
            {
                "id": "9998887770000",
                "marketplaceId": NULL,
                "type": "DISPLAY"
            }
            {
                "id": "9998887770001",
                "type":"DISPLAY"
            },
        ],
        "advertisersToRemove": []
    }
}
```
#### Multiple advertiser addition approval

When verifying multiple advertiser additions in a request, AMC validates and approves the advertiser Ids addition requests as described below:

**Approval for multiple sponsored ads entities added to an instance**

For requests with multiple sponsored ads entities for inclusion in an instance, AMC first performs the standard [admin user access verification](/API/docs/en-us/guides/amazon-marketing-cloud/admin/instance-management#admin-user-access-verification-amc-accounts). Then, AMC will verify the relationship of the requesting admin user with the advertiser.

If AMC cannot programmatically confirm the relationship of the requesting admin user with the advertiser Ids, the request will require a manual review. The AMC team will evaluate the relationship of the requesting admin user within 2 business days and then send either an approval or rejection notification.
You can check the status of your request using the `GET /amc/instances/{instanceId}/advertisers/updates/{updateId}` endpoint. This endpoint requires the `updateId` from your `POST` request.
If the manual review shows that the sponsored ads advertiser Ids are not linked to the account of the requesting admin user, the following error message shows up, and the request is rejected.

`This request was rejected because we were unable to confirm the advertiser accounts belong to the same brand for a single instance. Resubmit the request by adding each advertiser to a separate instance.`

Before resubmitting the request, ensure all the advertiser Ids belong to the same brand.

When both validations are successful, the request is approved automatically, and the sponsored ads advertiser Ids are added to the instance, with access to historical data (13 months to 5 years, depending on the data view).

**Approval for multiple Amazon DSP advertiser Ids to an instance**

Any requests for multiple DSP advertiser Ids additions go through the [admin user access verification](/API/docs/en-us/guides/amazon-marketing-cloud/admin/instance-management#admin-user-access-verification-amc-accounts).

* If AMC cannot validate the direct access of the requesting admin user to the advertiser Ids, the request will be sent for a manual approval, which is subject to a 2\-business days SLA.
* If the access of the requesting admin user is verified for the set of advertisers being added to the instance, the request returns a successful 200 response.

The successful advertiser addition request is then queued for a manual review to verify that all advertisers belong to the same brand.
You can check the status of your request within two business days of submission using the `GET /amc/instances/{instanceId}/advertisers/updates/{updateId}` endpoint. This endpoint requires the `updateId` from your `POST` request.

**Approval for agency or partner managed instances**

In case of agency or partner managed instances, AMC first checks if the agency or partner has the necessary permissions to access the data of the advertiser following the [admin user access verification](/API/docs/en-us/guides/amazon-marketing-cloud/admin/instance-management#admin-user-access-verification-amc-accounts).

 Important Before requesting advertiser inclusions to an instance, partner users must ensure that their advertiser client [LwA application must be linked to the partner account](/API/docs/en-us/guides/onboarding/assign-api-access#additional-recommended-steps-for-members-of-the-amazon-ads-partner-network) and that the AMC caller must be a user in the Partner Account.In addition, to obtaining the Login with Amazon (LwA) authorization to access the data of the advertiser, agency or partner users must do the following to establish the initial relationship with advertiser data:

* Make API calls on behalf of the advertiser. This can be done either through one campaign management call or two calls of any other type.
* Wait for the mandatory 3\-day period after the initial calls to allow AMC to establish and verify the connection between the partner LwA client ID and the account of the advertiser.
* Submit the request to add advertiser IDs of the client to the partner\-managed instance using the `POST/amc/instances/{instanceId}/advertisers/updates` endpoint.

 Note The initial API calls must have been made within the last 90 days.For sponsored ads advertiser inclusion, requests will be rejected if the access of the partner user cannot be verified.
For DSP advertiser inclusion requests, if AMC cannot verify the direct access of the requesting user through the [admin user access verification](/API/docs/en-us/guides/amazon-marketing-cloud/admin/instance-management#admin-user-access-verification-amc-accounts) process, the request will be sent for a manual approval, and may require a written confirmation from the advertiser authorizing your partnership.

 Important When modifying existing instances to include additional advertisers, only submit the new advertiser Ids. New advertisers undergo the same verification and approval process. All approved additions receive access to historical data, with retention of 13 months to 5 years depending on the data view. Refer to [AMC data retention](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/data-retention).### Retrieve advertiser update status

Use the `GET/amc/instances/{instanceId}/advertisers/updates` endpoint for details on advertiser update requests and statuses for a specific instance.

If you want to get details for a specific update request use the `GET /amc/instances/{instanceId}/advertisers/updates/{updateId}` operation.

The status of your update request could be one of the following:

* `PENDING`
* `UPDATING`
* `COMPLETED`
* `REJECTED`

Note that the numeral 0 (zero) will be considered as the first `updateId` and subsequent modification request ids will increment by 1\.

## Sandbox instances

All AMC accounts have automatic access to a sandbox instance. The sandbox instance provides a synthetic testing environment for hands\-on learning, signal investigation and query iteration without impacting live instances.

To identify your sandbox instance, use the `GET/amc/instances/{instanceId}` endpoint.
Your response body will contain the `instanceType` of each instance. The value for sandbox instances for the `instanceType` is `SANDBOX`.

Refer to the [AMC sandbox](/API/docs/en-us/guides/amazon-marketing-cloud/amc-sandbox) developer guide for more details.

## Collaboration instances

AMC customers can use AWS Clean Rooms for securely associating advertiser first\-party data to a collaboration and collecting data outputs from queries across their data and AMC data, without having to move any underlying data outside of their AWS environment.

AMC allows you to create an instance to create a collaboration with AWS Clean Rooms.

For more details, see [Set up a collaboration instance](/API/docs/en-us/guides/amazon-marketing-cloud/acr/4_setup_collab).

If you want to bring identity data to your collaboration, the following instances API endpoints will help you through the identity data upload process:

* `GET/amc/instances/{instanceId}/collaboration` to [retrieve your collaboration instance information](/API/docs/en-us/guides/amazon-marketing-cloud/acr/7_upload_identity#step-2-retrieve-your-collaboration-instance-information-instanceid).
* `POST/amc/instances/{instanceId}/collaboration/idnamespaces/list` to [retrieve a list of ID namespace **not** associated with a collaboration instance](/API/docs/en-us/guides/amazon-marketing-cloud/acr/7_upload_identity#step-3-retrieve-the-id-namespaces-associated-to-a-collaboration), so that you can select one of the not\-connected namespaces returned to create a mapping table.
* `POST /amc/instances/{instanceId}/collaboration/idmappingtables` [to create an ID mapping table](/API/docs/en-us/guides/amazon-marketing-cloud/acr/7_upload_identity#step-4-create-an-id-mapping-table).
* `GET /amc/instances/{instanceId}/collaboration/idmappingtables/{idMappingTableId}/jobs/{jobId}` [to retrieve the ID mapping job status for the requested AMC instance](/API/docs/en-us/guides/amazon-marketing-cloud/acr/7_upload_identity#step-5-retrieve-the-id-mapping-job-status).

After creating an ID mapping table, use the following endpoints to manage ID mapping tables.

| Endpoint | Description |
| --- | --- |
| `POST /amc/instances/{instanceId}/collaboration/idmappingtables/{idMappingTableId}/refresh` | Updates the data in the given ID. Mapping Table in the collaboration for the requested AMC instance. |
| `GET /amc/instances/{instanceId}/collaboration/idmappingtables/{idMappingTableId}/jobs/{jobId}` | Retrieves the ID mapping job metadata for the requested AMC instance. |
| `DELETE /amc/instances/{instanceId}/collaboration/idmappingtables/{idMappingTableId}` | Deletes the given ID Mapping Table in the collaboration for the requested AMC instance. |
