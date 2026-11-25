# Data uploads | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/advertiser-data-upload/adu-uploads

# Upload data to datasets

Was this page helpful? Note Looking for no\-code upload? See [Ads data manager](/API/docs/en-us/no-code-tools/adm/1_ads-data-manager-console-overview).The Upload API is used to manage the transfer of data to the dataset.

 Note When uploading, we recommend that individual files do not exceed 1GB.Before you begin uploading data, thoroughly read through [Prepare data](/API/docs/en-us/guides/amazon-marketing-cloud/advertiser-data-upload/advertiser-data-prepare-data) to understand guidelines and requirements for the files and data you will upload.

 WARNINGData that was uploaded using ADU 1\.0 can no longer be queried. To continue querying datasets that you had uploaded in ADU 1\.0, delete the previously uploaded data, and re\-upload using ADU 2\.0\.## Upload size recommendations

When uploading data to AMC, follow these size recommendations for optimal performance:

| Upload Type | Recommended Maximum |
| --- | --- |
| Individual file size | 1 GB |
| Total upload size | 50 GB |

### Uploading large datasets

For large datasets, split your data into multiple files (each no larger than 1 GB) and use either `sourceManifestS3Key` or `sourceS3Prefix` to upload them in a single API call (up to 50 GB per upload). For datasets exceeding 50 GB, split across multiple uploads as shown in the example below.

**Choosing the right approach based on data size:**

**Example: Uploading 60 GB of data**

**✅ Right approach:**

Split your 60 GB into files (≤1 GB each), then group them into uploads of \~20 GB each. This results in only 3 API calls instead of 60\.

When splitting into multiple uploads:
1\. To replace existing data:
\- First upload: `FULL_REPLACE`
\- Remaining uploads: `ADDITIVE`
2\. To add to existing data:
\- All uploads: `ADDITIVE`

**❌ Wrong approach:**

Do not create a separate API call for each file. If you have 60 GB of data split into 60 files (1 GB each), making 60 separate API calls is inefficient and not recommended.

This approach creates unnecessary overhead and may hit rate limits.### What to avoid

* Uploading a single file larger than 1 GB
* Creating many separate API calls for a single dataset
* Exceeding 50 GB in a single upload

### Supported Methods

| Method | Endpoint | Description |
| --- | --- | --- |
| [POST](/API/docs/en-us/amc-advertiser-data-upload#tag/Upload/operation/CreateUpload) | [/amc/advertiserData/{instanceId}/uploads/{dataSetId}](/API/docs/en-us/amc-advertiser-data-upload#tag/Upload/operation/CreateUpload) | Create new upload |
| [POST](/API/docs/en-us/amc-advertiser-data-upload#tag/Upload/operation/ListUploads) | [/amc/advertiserData/{instanceId}/uploads/list](/API/docs/en-us/amc-advertiser-data-upload#tag/Upload/operation/ListUploads) | Retrieve a paginated list of uploads for an instance |
| [GET](/API/docs/en-us/amc-advertiser-data-upload#tag/Upload/operation/GetUpload) | [/amc/advertiserData/{instanceId}/uploads/{dataSetId}/{uploadId}](/API/docs/en-us/amc-advertiser-data-upload#tag/Upload/operation/GetUpload) | View status and other details of an upload operation |

### Creating an upload

After you have [created a dataset](/API/docs/en-us/guides/amazon-marketing-cloud/advertiser-data-upload/advertiser-data-sets), upload data to the dataset using the following endpoint with the `dataSetId` in the path, as well as the request body.

```
POST /amc/advertiserData/{instanceId}/uploads/{dataSetId}
```
**Sample request body**

```
{
  "updateStrategy": "ADDITIVE",
  "countryCode": "US",
  "compressionFormat": "GZIP",
  "dataSource": {
    "sourceS3Bucket": "S3Bucket",
    "sourceFileS3Key": "S3Key"
  },
  "fileFormat": {
    "csvDataFormat": {
      "fieldDelimiter": ","
    }
  }
}
```
A successful call will return the status of the upload and an `uploadId`.

**Sample response**

```
{
  "status": "PENDING",
  "uploadId": "5f384873-1234-1234-1234-3738f7eb74ae"
}
```
#### S3 Bucket source

This Create Upload API call requires you to specify where the data is stored to be uploaded.

1. First, you will specify the `sourceS3Bucket`. This is the S3 bucket name.
2. Then you will specify which files or objects to upload. Your options include:

	* `sourceFileS3Key`: Used to specify a single file (for example, `"sourceFileS3Key" : "uploadFile.csv.gz"`) in the `sourceS3Bucket` to upload to AMC.
	* `sourceS3Prefix`: Used to specify multiple S3 objects rooted at a single S3 prefix. Learn more about [S3 prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html).
	* `sourceManifestS3Key`: Used to specify a manifest file, which is a file that points to multiple, distinct S3 objects. For example, you could specify the manifest file `"sourceManifestS3Key" : "manifestForAMCUpload.txt"` which points to other objects. See below for an example manifest file format.

**Manifest file format**

The following is the format of a manifest file.

```
s3://<s3bucketname1>/<pathKey1>/<fileName1>
s3://<s3bucketname2>/<pathKey2>/<fileName2>
s3://<s3bucketname3>/<pathKey3>/<fileName3>
s3://<s3bucketname4>/<pathKey4>/<fileName4>
```
 Note Note that the file names of files you are uploading in the `sourceS3Bucket`, irrespective of the key type provided (`sourceFileS3Key`, `sourcePrefixKey`, or `sourceManifestS3Key`), cannot start with a `.` (period character) or `_` (underscore character).#### Update strategies

The `updateStrategy` parameter allows you to specify how the new data will be merged with existing data in the dataset. The valid options are:

* `ADDITIVE`
* `FULL_REPLACE`
* `OVERLAP_REPLACE`
* `OVERLAP_KEEP`

**`ADDITIVE`**
**For fact datasets**: This strategy adds new records to records that may already be present in each time\-based partition of the table. If the table already contains records, then the (new) record set being uploaded may overlap with the existing records. These overlaps are partition overlaps.

For example, if the table contains time\-based data that is partitioned on month, and the table already holds data for the months January, February, March, then when a new upload containing data for March, April, May is performed with the `ADDITIVE` strategy, then records that will fall within the March partition will overlap with a partition where data already exists.

**`ADDITIVE`**
**For dimension datasets**: Dimension datasets are a single partition of records. This strategy, when used with a dimension dataset, will add the uploaded records to the existing records.

**`FULL_REPLACE`**
**For fact datasets**: The uploaded data replaces all records previously saved in the tables.

**`FULL_REPLACE`**
**For dimension datasets**: Dimension datasets have a single partition of records. This strategy will replace all existing records in that partition with the records to be uploaded.

**`OVERLAP_REPLACE`This strategy applies for uploads to fact datasets only. When a data upload is performed with `OVERLAP_REPLACE` as the strategy, then new data will be added to table partitions. Any overlapping partitions will be removed and** replaced **with new content.

For example, previously uploaded monthly data contains records in the February, March, and April partitions. Data being uploaded should fall into April and May. With this option, any prior events in April will be** removed, and replaced with the data for April from the new upload, and May will be added directly, as there is no overlap with existing data.

**`OVERLAP_KEEP`This strategy applies for uploads to fact datasets only. All new data for non\-overlapping partitions will be added to the table. Any overlapping partitions will retain their original data. When the upload overlaps with any partitions that already have data, the original data of the overlapping partition(s) is RETAINED, and those in the upload are ignored. For example, if the dataset has previously uploaded monthly data, in the February, March, and April partitions. A new upload containing data for April and May is performed. When uploaded with `OVERLAP_KEEP` as the upload strategy, any existing data for April will be retained, and those corresponding to April in the new upload will be** ignored. Data for May will be added directly, as there is no overlap with the existing data.

#### Setting the country code at upload\-level

You can specify the country code for an upload.

 Note You can also set the country code on the row\-level or dataset\-level. Refer to [Setting the country code (row\-level or dataset\-level)](/API/docs/en-us/guides/amazon-marketing-cloud/advertiser-data-upload/advertiser-data-sets#setting-the-country-code).Add the following attribute to the upload creation:

```
"countryCode" : "US"
```
 Note This is an example of setting the country code to `US`. Replace US with the appropriate 2\-character string in the ISO 3166 format.
```
{
  "updateStrategy": "ADDITIVE",
  "countryCode": "US",
  "compressionFormat": "BZIP",
  "dataSource": {
    ...
  },
  "fileFormat": {
    ...
  }
}
```
### View all uploads

Returns a list of all uploads, as well as the upload details.

```
POST /amc/advertiserData/{instanceId}/uploads/list
```
**Sample response**

```
{
  "uploads": [
    {
      "createdAt": "2023-09-29T17:36:32Z",
      "metrics": {
        "OutputRowCount": 1782332
      },
      "status": "COMPLETED",
      "updatedAt": "2023-09-29T17:51:30Z",
      "uploadId": "2dd474b2-1234-1234-1234-eafe9ccc216c"
    },
    {
      "createdAt": "2023-09-29T17:58:45Z",
      "message": "No such file or directory 's3://myS3bucket'",
      "metrics": {},
      "status": "FAILED",
      "updatedAt": "2023-09-29T18:04:26Z",
      "uploadId": "c83cd17b-1234-1234-1234-db6424aab1c3"
    }
  ]
}
```
### View a specific upload

To get details about a specific upload, use the following operation:

```
GET /amc/advertiserData/{instanceId}/uploads/{dataSetId}/{uploadId}
```
**Sample response**

```
{
  "upload": {
    "createdAt": "2023-09-29T17:36:32Z",
    "metrics": {
      "OutputRowCount": 1782332
    },
    "status": "COMPLETED",
    "updatedAt": "2023-09-29T17:51:30Z",
    "uploadId": "2dd474b2-1234-1234-1234-eafe9ccc216c"
  }
}
```
## Viewing and using the uploaded dataset in the AMC UI

Once the upload status is returned as `COMPLETED`, you will be able to see the uploaded data in the Advertiser uploaded section of the Schema explorer.

You will also be able to run SQL queries using the dataset both in the Query Editor in the AMC UI and using the [Workflow management service APIs](/API/docs/en-us/guides/amazon-marketing-cloud/reporting/workflow-management-service).## Next steps

If you need to modify columns in the dataset, refer to [Data set columns API](/API/docs/en-us/guides/amazon-marketing-cloud/advertiser-data-upload/advertiser-data-column).
