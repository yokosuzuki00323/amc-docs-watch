# Data deletion | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/advertiser-data-upload/advertiser-data-identity-deletion

# Advertiser data identity deletion

Was this page helpful?This set of resources allows you to create a request for user deletion of a set of hashed target identity fields and values in all datasets. You can also retrieve the deletion requests and get the status of your request.

 Note Identity deletion accepts the same set of identities that are accepted at upload time. For IP addresses, this means deletion supports all 4 combinations: raw (plaintext) IPv4, hashed IPv4, raw (plaintext) IPv6, and hashed IPv6 (see [Prepare your data](/API/docs/en-us/guides/amazon-marketing-cloud/advertiser-data-upload/advertiser-data-prepare-data#id-resolution-and-supported-identifiers)). To delete an uploaded IP address identity, submit the same value (hashed or plaintext) that was originally uploaded.### Supported Methods

| Methods | Endpoint | Description |
| --- | --- | --- |
| [POST](/API/docs/en-us/amc-advertiser-data-upload#tag/User-Deletion-Request/operation/CreateUserDeletionRequest) | [/amc/advertiserData/{instanceId}/userDeletionRequest](/API/docs/en-us/amc-advertiser-data-upload#tag/User-Deletion-Request/operation/CreateUserDeletionRequest) | Creates a request for user deletion of a set of hashed target identity fields and values in all data sets. |
| [POST](/API/docs/en-us/amc-advertiser-data-upload#tag/User-Deletion-Request/operation/ListUserDeletionRequests) | [/amc/advertiserData/{instanceId}/userDeletionRequest/list](/API/docs/en-us/amc-advertiser-data-upload#tag/User-Deletion-Request/operation/ListUserDeletionRequests) | Gets a paginated list of all user deletion requests. |
| [GET](/API/docs/en-us/amc-advertiser-data-upload#tag/User-Deletion-Request/operation/GetUserDeletionRequest) | [/amc/advertiserData/{instanceId}/userDeletionRequest/{userDeletionRequestId}](/API/docs/en-us/amc-advertiser-data-upload#tag/User-Deletion-Request/operation/GetUserDeletionRequest) | Gets status and metadata for a previously initiated identity deletion. |
