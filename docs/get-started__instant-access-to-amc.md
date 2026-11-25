# Get access to AMC using self-service APIs | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/get-started/instant-access-to-amc

# Instant self\-service access to AMC

Was this page helpful?If you have a sponsored ads account or a global advertising account, you can use AMC instant self\-service access to automatically create an AMC instance associated with that account, allowing you access to AMC within minutes. The instance is scoped to that single advertiser.

## Requirements

* Customers have onboarded to Amazon Ads API. For more information, refer to [Get started](/API/docs/en-us/guides/amazon-marketing-cloud/get-started/get-started).
* Customer must have a sponsored ads account (and know its sponsored ads entity ID) or a global advertising account (and know its global advertising account ID, which begins with `amzn1.ads-account.g.`).

### Configure header parameters

 Note Set the `Amazon-Advertising-API-AdvertiserId` header to your advertiser account ID — the sponsored ads entity ID for a sponsored ads account, or the global advertising account ID (beginning with `amzn1.ads-account.g.`) for a global advertising account (not the AMC account ID). All other header parameters are standard.

| Header | Description |
| --- | --- |
| `Amazon-Advertising-API-ClientId` | The client ID related to a Login with Amazon application. |
| `Amazon-Advertising-API-MarketplaceId` | The marketplace identifier for the marketplace of the advertiser. For global advertising accounts, always use US (`ATVPDKIKX0DER`). |
| `Amazon-Advertising-API-AdvertiserId` | Your advertiser account ID: the sponsored ads entity ID for a sponsored ads account, or the global advertising account ID (beginning with `amzn1.ads-account.g.`) for a global advertising account. This is not an AMC entity ID. Use it for API calls to instances created with AMC instant self\-service access APIs. |
| `Authorization` | Login with Amazon token in the form of `Bearer {token}`. |

 Note This page covers instant self\-service access, which applies to sponsored ads accounts and global advertising accounts. Manager accounts use account\-based access, not this flow; for the manager account header parameters, see [Make your first call](/API/docs/en-us/guides/amazon-marketing-cloud/get-started/make-your-first-call#header-parameters).## Get access to your instance

1. Use the `GET /amc/instances` endpoint to retrieve your instance.
2. If you receive the message "Terms and conditions must be accepted to continue," you must accept the terms and conditions before you can proceed. Log into the AMC UI using the email address that is associated with Login with Amazon. If you have not logged into the AMC UI before, you will need to create an account using the email address associated with Login with Amazon. AMC terms and conditions must be accepted once in each region (NA, EU, and FE) where the AMC instance is going to be created and accessed.

**Sample response**

```
{
  "instances": [
    {
      "instanceId": "amcabcdefgh",
      "instanceName": "amcabcdefgh",
      "instanceType": "STANDARD",
      "customerCanonicalName": "sponsored ads user",
      "creationStatus": "IN_PROGRESS",
      "creationDatetime": "2025-01-01T00:00:00.000000000Z",
      "s3BucketName": "",
      "awsAccountId": "",
      "entities": [
        "NA"
      ],
      "dataUploadAwsAccountId": "012345678910",
      "apiEndpoint": "https://advertising-api.amazon.com",
      "acrCollaboration": null,
      "optionalDatasets": [
        ...
      ],
      "advertiserTypes": [
        "SPONSORED_ADS"
      ]
    }
  ],
  "nextToken": null
}
```
3. Continue to call the `GET /amc/instances` endpoint in a loop until the `creationStatus` is `COMPLETED`. AMC instance creation takes up to 300 seconds.

**Sample response**

```
{
  "instances": [
    {
      "instanceId": "amcabcdefgh",
      "instanceName": "amcabcdefgh",
      "instanceType": "STANDARD",
      "customerCanonicalName": "sponsored ads user",
      "creationStatus": "COMPLETED",
      "creationDatetime": "2025-01-01T00:00:00.000000000Z",
      "s3BucketName": "",
      "awsAccountId": "",
      "entities": [
        "NA"
      ],
      "dataUploadAwsAccountId": "012345678910",
      "apiEndpoint": "https://advertising-api.amazon.com",
      "acrCollaboration": null,
      "optionalDatasets": [
        ...
      ],
      "advertiserTypes": [
        "SPONSORED_ADS"
      ]
    }
  ],
  "nextToken": null
}
```
4. The instance created will be a standard AMC instance. Note that Sandbox and collaboration instances are not created using the self\-service APIs.
5. Once it is complete, you are ready to access the instance using AMC APIs. Note the supported and unsupported endpoints listed below.

## Supported/unsupported endpoints

### Supported

Most AMC APIs are supported when using an instant self\-service access instance, including reporting and audiences APIs. The following table outlines the AMC administration APIs that are supported with self\-service instances.

Note: This is not an exhaustive list of supported endpoints.

| Endpoints |
| --- |
| `GET /amc/instances` |
| `GET /amc/instances/{instanceId}` |
| `PUT /amc/instances/{instanceId}` (Supported for updating `awsAccountId`, `s3BucketName`, and `instanceName`) |
| `GET /amc/instances/{instanceId}/advertisers` |

### Not supported

With self\-service instances, operations like creating new instances, deleting instances, adding advertisers to instances, and other instance, account, and user modifications are not supported. The following table lists the AMC administration endpoints that are not supported.

Using the following endpoints for an on\-demand instance is not supported and will return `400`.

| Endpoints |
| --- |
| `PUT /amc/instances/{instanceId}` (Not supported for updating `advertiserName`) |
| `POST /amc/instances` |
| `DELETE /amc/instances/{instanceId}` |
| `GET /amc/instances/{instanceId}/advertisers/updates` |
| `GET /amc/instances/{instanceId}/advertisers/updates/{update}` |
| `POST /amc/instances/{instanceId}/advertisers/updates` |

Additionally, access to [the advertiser data upload APIs](/API/docs/en-us/guides/amazon-marketing-cloud/advertiser-data-upload/advertiser-data-overview) is not supported for self\-service instances. The following data upload operations will return a `400`.

| Endpoints |
| --- |
| `POST /amc/advertiserData/{instanceId}/dataSets` |
| `POST /amc/advertiserData/{instanceId}/dataSets/list` |
| `DELETE /amc/advertiserData/{instanceId}/dataSets/{dataSetId}` |
| `GET /amc/advertiserData/{instanceId}/dataSets/{dataSetId}` |
| `PUT /amc/advertiserData/{instanceId}/dataSets/{dataSetId}` |
| `POST /amc/advertiserData/{instanceId}/dataSets/{dataSetId}/columns` |
| `DELETE /amc/advertiserData/{instanceId}/dataSets/{dataSetId}/columns/{columnName}` |
| `PUT /amc/advertiserData/{instanceId}/dataSets/{dataSetId}/columns/{columnName}` |
| `POST /amc/advertiserData/{instanceId}/uploads/{dataSetId}` |
| `POST /amc/advertiserData/{instanceId}/uploads/list` |
| `GET /amc/advertiserData/{instanceId}/uploads/{dataSetId}/{uploadId}` |
| `POST /amc/advertiserData/{instanceId}/userDeletionRequest` |
| `POST /amc/advertiserData/{instanceId}/userDeletionRequest/list` |
| `GET /amc/advertiserData/{instanceId}/userDeletionRequest/{userDeletionRequestId}` |
