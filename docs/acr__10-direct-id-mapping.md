# Resolve third-party identities with Direct ID Mapping | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/acr/10-direct-id-mapping

# Resolve third\-party identities with Direct ID Mapping

Was this page helpful?Direct ID Mapping lets Amazon Marketing Cloud (AMC) customers on AWS Clean Rooms join event data that already carries a third\-party identity directly against Amazon\-owned datasets, without setting up an AWS Entity Resolution (AER) workflow. You bring your event data through an AMC on AWS Clean Rooms Configured Table with the identity value in a standard\-named column, and AMC resolves it to the Amazon user behind the scenes with no changes to your query required.

 Note Direct ID Mapping is only supported for United States (US) identities. Identities from other regions will not be matched.## How it works

When you register event data as an AMC on AWS Clean Rooms Configured Table, AMC looks for columns in your dataset that match the naming convention for a supported identity type (see [Sentinel column registry](/API/docs/en-us/guides/amazon-marketing-cloud/acr/10-direct-id-mapping#sentinel-column-registry) below). If it finds one, it automatically injects the resolution join when you query. You continue to write a standard `user_id` join, and AMC rewrites it to resolve through the matching Amazon\-owned mapping table.

If your dataset includes more than one supported identity column (for example, both a LiveRamp RampID column and a MAID column), AMC resolves them using a fixed priority order via `COALESCE`, so the highest\-confidence available match is used for each row. See [Resolution priority order](/API/docs/en-us/guides/amazon-marketing-cloud/acr/10-direct-id-mapping#resolution-priority-order) below.

## Setup

1. **Name the sentinel column** (the identity column with the AMC\-reserved name for that identity type) on your event dataset. See the [Sentinel column registry](/API/docs/en-us/guides/amazon-marketing-cloud/acr/10-direct-id-mapping#sentinel-column-registry) table below for the exact column name to use.
2. **Register your event data as an AMC on AWS Clean Rooms Configured Table** and associate it with your AMC\-managed collaboration. This is the standard AMC on AWS Clean Rooms event\-upload flow. Refer to [Upload event data](/API/docs/en-us/guides/amazon-marketing-cloud/acr/6_upload_event).
3. **Write a `user_id` join.** No special syntax is required. AMC detects the identity column automatically and injects the resolution join. You do not need to write the resolution join yourself.

## Supported identity types

The following identity types are supported by Direct ID Mapping.

 Important **Household identifiers are not supported.** Household\-level identity columns (for example, Experian, TransUnion, or SambaTv household IDs) are **not** supported by Direct ID Mapping. Do not use household identity values in these columns.### Sentinel column registry

| Sentinel column name | Identity type | Mapping |
| --- | --- | --- |
| `customer_raw_ip_address` | Raw (plaintext) IP address | IP address → Amazon user or IP address. See [Resolve IP addresses](/API/docs/en-us/guides/amazon-marketing-cloud/acr/11-ip-joins) for full setup, including RFC 5952 normalization requirements. |
| `customer_hashed_ip_address` | Hashed IP address | IP address → Amazon user or IP address. See [Resolve IP addresses](/API/docs/en-us/guides/amazon-marketing-cloud/acr/11-ip-joins) for full setup, including RFC 5952 normalization and hashing requirements. |
| `customer_maid_id` | Mobile Advertising ID (MAID) | MAID device → Amazon user |
| `customer_liveramp_id` | LiveRamp RampID | LiveRamp user → Amazon user |
| `customer_experian_id` | Experian user | Experian user → Amazon user |
| `customer_transunion_id` | TransUnion user | TransUnion user → Amazon user |
| `customer_sambatv_acr_id` | SambaTv ACR user | SambaTv ACR user → Amazon user |

 Note **Transcoding requirement for Experian, LiveRamp, and TransUnion.** Before placing these identifiers in a sentinel column, the raw vendor ID must be transcoded to Amazon's namespace through the same vendor\-transcoding relationship already described in [Bring identity data into the collaboration instance](/API/docs/en-us/guides/amazon-marketing-cloud/acr/7_upload_identity). An un\-transcoded raw ID (for example, a raw RampID that hasn't gone through this process) will not resolve. This requirement does **not** apply to MAID, SambaTv ACR, or either IP sentinel column, none of which require vendor\-side transcoding. Note **Full IP setup lives on a separate page.** The two IP rows above are included here so this table reflects every supported sentinel column, but normalization, hashing, and other IP\-specific setup steps are documented in full on [Resolve IP addresses](/API/docs/en-us/guides/amazon-marketing-cloud/acr/11-ip-joins), since that page also covers IP\-to\-IP joins, which don't use these sentinel columns at all. See [Resolution priority order](/API/docs/en-us/guides/amazon-marketing-cloud/acr/10-direct-id-mapping#resolution-priority-order) below for how IP ranks against the other identity types.## Resolution priority order

If a dataset contains more than one supported identity column, or both AWS Entity Resolution and one or more sentinel columns, AMC resolves identities in the following fixed priority order. The highest\-priority available match for each row is used.

| Priority | Identity source | Sentinel / source column |
| --- | --- | --- |
| 1 | AWS Entity Resolution ID mapping table | `customer_user_id` (via `user_id_mapping`) |
| 2 | Raw IP address | `customer_raw_ip_address` (\+ `customer_event_time`) |
| 3 | Hashed IP address | `customer_hashed_ip_address` (\+ `customer_event_time`) |
| 4 | Mobile Advertising ID (MAID) | `customer_maid_id` |
| 5 | LiveRamp RampID | `customer_liveramp_id` |
| 6 | Experian user | `customer_experian_id` |
| 7 | TransUnion user | `customer_transunion_id` |
| 8 | SambaTv ACR user | `customer_sambatv_acr_id` |

## Example event data

The tables below show sample `my_events` datasets with sentinel columns populated. In both cases, you query this data with the same standard `user_id` join shown in [Query example](/API/docs/en-us/guides/amazon-marketing-cloud/acr/10-direct-id-mapping#query-example) below. AMC detects the sentinel columns automatically.

**Example 1: A single sentinel column (LiveRamp)**

| event\_id | event\_time | customer*liveramp*id | advertiser\_id |
| --- | --- | --- | --- |
| evt\_1001 | 2026\-09\-14T10:15:00Z | RAMP\_8f2a91c3 | ADV\_4521 |
| evt\_1002 | 2026\-09\-14T11:42:00Z | RAMP\_3b7d14e0 | ADV\_4521 |

**Example 2: Multiple sentinel columns (MAID and Experian)**

| event\_id | event\_time | customer*maid*id | customer*experian*id | advertiser\_id |
| --- | --- | --- | --- | --- |
| evt\_2001 | 2026\-09\-14T09:05:00Z | a1b2c3d4\-e5f6\-7890 |  | ADV\_7733 |
| evt\_2002 | 2026\-09\-14T09:47:00Z |  | EXP\_90213f | ADV\_7733 |
| evt\_2003 | 2026\-09\-14T10:12:00Z | a1b2c3d4\-f1a2\-3344 | EXP\_55102a | ADV\_7733 |

 Note A row does not need every sentinel column populated. AMC resolves each row using whichever supported identity column has a value, following the priority order described in [Resolution priority order](/API/docs/en-us/guides/amazon-marketing-cloud/acr/10-direct-id-mapping#resolution-priority-order) above. When a row has **more than one** sentinel column populated, as in `evt_2003` above, AMC picks the first non\-null identity type by priority order; here, MAID (priority 4\) is used instead of Experian (priority 6\), since MAID ranks higher.## Query example

Write a standard `user_id` join and AMC automatically detects which supported identity columns are present on your dataset (whether that's AWS Entity Resolution, one or more sentinel columns, or a combination) and resolves identities accordingly. Your query is the same regardless of which identity columns are present.

```
SELECT d.advertiser_id,
       COUNT(*) AS matched_impressions
FROM   my_events e
JOIN   dsp_impressions d
  ON   e.user_id = d.user_id
GROUP BY d.advertiser_id;
```
 Note **Important:** You always write a simple `JOIN ... ON user_id = user_id`. AMC handles identity resolution automatically for any supported identity column present on your dataset. Do not attempt to write the resolution joins yourself.
