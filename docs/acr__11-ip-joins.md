# Resolve IP addresses in AMC on AWS Clean Rooms | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/acr/11-ip-joins

# Resolve IP addresses in AMC on AWS Clean Rooms

Was this page helpful?AMC on AWS Clean Rooms supports IP address–based attribution joins, letting you match first\-party event data against Amazon\-owned datasets (such as DSP impressions) using IPv4 or IPv6 addresses, in addition to the identity types covered by [AWS Entity Resolution](/API/docs/en-us/guides/amazon-marketing-cloud/acr/7_upload_identity) and [Direct ID Mapping](/API/docs/en-us/guides/amazon-marketing-cloud/acr/10-direct-id-mapping).

## Supported join types

AMC on AWS Clean Rooms supports the following IP address join types:

* **IPv4\-to\-IPv4**: Match your first\-party IPv4 address directly against the IPv4 address on an Amazon\-owned dataset (such as DSP impressions). The join resolves to a matched row, not to a `user_id`.
* **IPv4\-to\-user\_id**: Resolve your first\-party IPv4 address to the Amazon `user_id` behind it, so you can join on `user_id` the same way you would with any other supported identity type.
* **IPv6\-to\-user\_id**: Resolve your first\-party IPv6 address to the Amazon `user_id` behind it, so you can join on `user_id` the same way you would with any other supported identity type.
* **IPv6\-to\-IPv6**: Match your first\-party IPv6 address directly against the IPv6 address on an Amazon\-owned dataset (such as DSP impressions). The join resolves to a matched row, not to a `user_id`.

Each join type works with either **raw (plaintext)** or **hashed** IP addresses. See [Setup](/API/docs/en-us/guides/amazon-marketing-cloud/acr/11-ip-joins#setup) below for the corresponding sentinel column to use for each format.

## Setup

Configure your event data with the following sentinel columns:

| Sentinel column name | Purpose |
| --- | --- |
| `customer_raw_ip_address` | Plaintext (unhashed) IPv4 or IPv6 address. IPv6 addresses must be RFC 5952\-normalized; IPv4 does not require normalization. See [IP address standardization and hashing](/API/docs/en-us/guides/amazon-marketing-cloud/acr/11-ip-joins#ip-address-standardization-and-hashing) below for details. |
| `customer_hashed_ip_address` | SHA\-256 hashed IPv4 or IPv6 address (IPv6 must be RFC 5952\-normalized before hashing) |
| `customer_event_time` | Event timestamp (required for time\-bound IP\-to\-user\_id resolution to scope the join) |

When AMC detects these columns on an AMC on AWS Clean Rooms Configured Table, the AMC compiler automatically generates the virtual columns needed to power the supported IP\-to\-IP and IP\-to\-user\_id joins against Amazon DSP impression data. You do not need to write the resolution join yourself, consistent with [Direct ID Mapping](/API/docs/en-us/guides/amazon-marketing-cloud/acr/10-direct-id-mapping).

**Prerequisites:**

* An AMC on AWS Clean Rooms instance
* An AWS Clean Rooms collaboration
* Your IP addresses prepared according to the standardization and hashing rules below

### IP address standardization and hashing

* **Plaintext IP addresses** (`customer_raw_ip_address`) must be normalized to the RFC 5952 canonical text representation before upload.
* **Hashed IP addresses** (`customer_hashed_ip_address`) must be SHA\-256 hashed, after first normalizing to the RFC 5952 canonical form. Hashing an IP address without normalizing it first produces a hash that AMC cannot resolve.

You can utilize the [AMCFilePreparationTool](https://public-file-hosting-repository.s3.amazonaws.com/File+Preparation+Tool.zip) to normalize and hash your data.

| Step | Requirement |
| --- | --- |
| 1\. Normalize | Normalize the IPv6 address to its RFC 5952 canonical text representation. IPv4 does not need to be normalized. |
| 2\. Hash (hashed addresses only) | Apply SHA\-256 to the normalized address. Skip this step for plaintext addresses. |
| 3\. Populate | Place the result in `customer_raw_ip_address` (plaintext) or `customer_hashed_ip_address` (hashed), as appropriate. |

## Resolution priority

The fixed\-priority `COALESCE` chain described in [Direct ID Mapping: Resolution priority order](/API/docs/en-us/guides/amazon-marketing-cloud/acr/10-direct-id-mapping#resolution-priority-order) applies specifically to **IP\-to\-user\_id** resolution (IPv4\-to\-user*id, IPv6\-to\-user*id) and the third\-party identity types (MAID, LiveRamp, Experian, TransUnion, SambaTv ACR). For these join types, raw IP address is tried before hashed IP address, and both are tried before any third\-party sentinel identity column, exactly as in Direct ID Mapping.

**IPv4\-to\-IPv4 and IPv6\-to\-IPv6 joins do not go through this chain.** An IP\-to\-IP join matches directly on the IP address column rather than resolving to a `user_id`, so the query is different. See [Query examples](/API/docs/en-us/guides/amazon-marketing-cloud/acr/11-ip-joins#query-examples) below.

## Query examples

### IPv4\-to\-user*id / IPv6\-to\-user*id

Resolving an IP address to a `user_id` uses the same automatic resolution as other supported identity types: write a standard `user_id` join, and AMC resolves it using the priority order above.

```
SELECT d.advertiser_id,
       COUNT(*) AS matched_impressions
FROM   my_events e
JOIN   dsp_impressions d
  ON   e.user_id = d.user_id
GROUP BY d.advertiser_id;
```
### IPv4\-to\-IPv4 / IPv6\-to\-IPv6

IP\-to\-IP joins are not auto\-resolved to a `user_id`; write an explicit join condition on the IP address columns. The example below also matches on `user_id` in the same query, so a row counts as a match through either path:

```
SELECT
    COALESCE(d.user_id, e.user_id) AS matched_user,
    COUNT(*) AS impression_count
FROM   my_events e
JOIN   dsp_impressions d
    ON d.user_id = e.user_id
    OR d.ip_address = e.ip_address
GROUP BY COALESCE(d.user_id, e.user_id);
```
## Limitations

* See [Direct ID Mapping](/API/docs/en-us/guides/amazon-marketing-cloud/acr/10-direct-id-mapping) and [AWS Entity Resolution](/API/docs/en-us/guides/amazon-marketing-cloud/acr/7_upload_identity) for identity types outside of IP address.
