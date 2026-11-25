# Overview | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/datasources/overview

# Amazon Marketing Cloud data sources

Was this page helpful?Data from your Amazon Ads campaign events are ingested into AMC. This data could be from ad activity on Amazon DSP and sponsored ads, and can be referenced through the following tables:

* [Amazon DSP traffic](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/overview#amazon-dsp-traffic-tables)
* [Amazon Ads conversions](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/overview#amazon-ads-conversion-tables)
* [Sponsored ads](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/overview#sponsored-ads-table)
* [Amazon Live traffic](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/overview#amazon-live-traffic-table)
* [AMC Paid features](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/overview#amc-paid-features)
* [AMC audiences tables](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/overview#amc-audiences-tables)

All tables have a flat schema consisting of a list of columns that each have a name, a data type, a column type of metric or dimension, and an aggregation threshold. For details, see [AMC data aggregation thresholds](/API/docs/en-us/guides/amazon-marketing-cloud/aggregation-threshold).

Creating or modifying materialized tables is not supported in AMC SQL. The only supported operations are queries that operate on defined tables within AMC. Tables in AMC can be queried like SQL tables.

In addition, AMC also supports for your subscriptions through Paid Features. You can also upload your own datasets.

## Amazon DSP traffic tables

The following tables contain inputs from all Amazon DSP campaigns from the DSP advertising accounts that have been added to this instance. Includes records from ad product types such as Display, Online Video, Streaming TV, Audio, etc.

* [Amazon DSP impressions](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/dsp_impressions)
* [Amazon DSP clicks](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/dsp_clicks)
* [Amazon DSP views](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/dsp_views)
* [Amazon DSP impressions by segments](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/dsp_impressions_by_segments)

## Amazon Ads conversion tables

These tables both contain pairs of traffic and conversion events. "Traffic events" are impressions and clicks. "Conversion events" include purchases, various interactions with Amazon website, such as detailed page views and pixel fires. Each conversion event in the table is attributed to its corresponding traffic event.

* [Conversions](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/conversions)
* [Conversions with relevance](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/conversions_with_relevance)
* [Amazon attributed events by conversion time](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/amazon_attributed_events_by_conversion_time)

## Sponsored ads table

This table includes both impressions and clicks for sponsored ads programs.

* [Sponsored ads traffic table](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/sponsored_ads_traffic)

## Amazon Live traffic table

This table includes Amazon Live impression, click, and view events, reported at the granularity of the carousel ads that are displayed alongside the Amazon Live broadcast media.

* [Amazon Live traffic table](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/amazon_live_traffic)

## AMC paid features

The following tables contain signals associated with AMC paid features. For more information about availability and eligibility, refer to [Paid features overview](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/paid_features_overview).

* [Conversions all](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/conversions_all_paid)
* [Amazon audience segment membership](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/audience_segment_membership_paid)
* [Amazon Your Garage](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/amazon_your_garage_paid)
* [Amazon Brand Store insights](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/brand_store_insights_paid)
* [Amazon Retail Purchase](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/amazon_retail_purchase_paid)
* [Amazon Prime Video Channel Insights](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/prime_video_channel_insights_paid)
* [Experian vehicle purchases](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/experian_paid)
* [NC Solutions (NCS) CPG Insights Stream](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/cpg_insights_stream_paid)

 Note Dataset availability can vary by the marketplace to which the AMC account belongs.## Demographic data not available

While demographic data (such as age, marital status, and income) is not available in AMC, you have the option to leverage your own first\-party demographic data. Ads data manager is an Amazon Ads offering that lets advertisers securely upload first\-party data through a console or APIs and share it with AMC and other Amazon Ads products. For more information, refer to [Ads data manager](/API/docs/en-us/no-code-tools/adm/1_ads-data-manager-console-overview).

## AMC Audiences tables

AMC Audiences uses a unique set of tables that mirror the data available in AMC for both Amazon Ads tables and Paid features tables.

### Amazon Ads audience tables

* `amazon_attributed_events_by_conversion_time_for_audiences`
* `amazon_attributed_events_by_traffic_time_for_audiences`
* `conversions_for_audiences`
* `conversions_with_relevance_for_audiences`
* `dsp_clicks_for_audiences`
* `dsp_impressions_by_matched_segments_for_audiences`
* `dsp_impressions_by_user_segments_for_audiences`
* `dsp_impressions_for_audiences`
* `dsp_views_for_audiences`
* `dsp_video_events_feed_for_audiences`
* `sponsored_ads_traffic_for_audiences`
* `amazon_live_traffic_for_audiences`

### Paid features audience tables

If the Paid feature is available in your region or marketplace and your instance is eligible, the audience table will be automatically available in your instance. For more information, refer to [Paid features overview](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/paid_features_overview).

* `conversions_all_for_audiences`
* `audience_segments_[amer|apac|eu]_inmarket_for_audiences`
* `audience_segments_[amer|apac|eu]_inmarket_snapshot_for_audiences`
* `audience_segments_[amer|apac|eu]_lifestyle_for_audiences`
* `audience_segments_[amer|apac|eu]_lifestyle_snapshot_for_audiences`
* `segment_metadata_for_audiences`
* `amazon_your_garage_for_audiences`
* `amazon_brand_store_page_views(_non_endemic)_for_audiences`
* `amazon_brand_store_engagement_events(_non_endemic)_for_audiences`
* `amazon_retail_purchases_for_audiences`
* `amazon_pvc_enrollments_for_audiences`
* `amazon_pvc_streaming_events_feed_for_audiences`

## Amazon Ad Server tables

 Important Amazon Ad Server was sunset in Q4 2024\. Please visit the [AAS offboarding information page](https://support.sizmek.com/hc/en-us/articles/21193881095565-AAS-offboarding-package) for offboarding support resources and sunset FAQs.## Important notes for querying data sets

### Time Zones

AMC queries are based on UTC time by default, but the advertising console provides reports based on advertiser time zone (for example, America/Los\_Angeles).

When working with AMC APIs, to match AMC to the advertiser time zone, the `timeWindowTimeZone` parameter of the `CreateWorkflowExecution` request can be used to specify the time zone.

### Arbitrary Attribution Intervals

In the API, there are four intervals metrics can be viewed at: `_1d`, `_7d`, `_14d`, `_30d`, but in AMC, a user can aggregate results for any interval up to the attribution window, which is 14d. For example, to get conversions that occurred within `_9d` of the traffic time, use the following SQL:

```
SELECT
  campaign,
  SUM(total_purchases) AS total_orders_9d
FROM
  amazon_attributed_events_by_traffic_time
WHERE
  SECONDS_BETWEEN(traffic_event_dt_utc, conversion_event_dt_utc) <= 60 * 60 * 24 * 9
GROUP BY
  campaign
```
Alternatively, fitting the same concept into a single expression:

```
SUM(IF(SECONDS_BETWEEN(traffic_event_dt_utc, conversion_event_dt_utc) <= 9 * 24 * 60 * 60, total_purchases_clicks, 0)) AS purchases_9d
```
### Conversion vs Traffic Time

As products and in the advertising console, Sponsored Products and Sponsored Display uses `amazon_attributed_events_by_traffic_time` and Sponsored Brands uses `amazon_attributed_events_by_conversion_time`.

### Sponsored Products Conversions and Traffic

The following example shows how to union conversions with Sponsored Products. Notice that we filter specifically for the ad product we care about here as seen by:

```
     WHERE
        ad_product_type = 'sponsored_products'
```
This ensures that we do not include display conversions, which currently has a null value for `ad_product_type`.

```
WITH traffic_and_conversion_events AS (
  SELECT
    advertiser,
    campaign,
    0 AS impressions,
    0 AS clicks,
    IF(
      SECONDS_BETWEEN(traffic_event_dt_utc, conversion_event_dt_utc) <= 60 * 60 * 24 * 7,
      total_purchases,
      0
    ) AS total_purchases_7d,
    IF(
      SECONDS_BETWEEN(traffic_event_dt_utc, conversion_event_dt_utc) <= 60 * 60 * 24 * 14,
      total_purchases,
      0
    ) AS total_purchases_14d,
    IF(
      SECONDS_BETWEEN(traffic_event_dt_utc, conversion_event_dt_utc) <= 60 * 60 * 24 * 14,
      purchases,
      0
    ) AS purchases_14d,
    IF(
      SECONDS_BETWEEN(traffic_event_dt_utc, conversion_event_dt_utc) <= 60 * 60 * 24 * 14,
      total_product_sales,
      0
    ) AS total_product_sales_14d,
    IF(
      SECONDS_BETWEEN(traffic_event_dt_utc, conversion_event_dt_utc) <= 60 * 60 * 24 * 14,
      total_units_sold,
      0
    ) AS total_units_sold_14d,
    IF(
      SECONDS_BETWEEN(traffic_event_dt_utc, conversion_event_dt_utc) <= 60 * 60 * 24 * 14,
      brand_halo_units_sold,
      0
    ) AS brand_halo_units_sold_14d
  FROM
    amazon_attributed_events_by_traffic_time
  WHERE
    ad_product_type = 'sponsored_products'
  UNION ALL
  SELECT
    advertiser,
    campaign,
    impressions,
    clicks,
    0 AS total_purchases_7d,
    0 AS total_purchases_14d,
    0 AS purchases_14d,
    0 AS total_product_sales_14d,
    0 AS total_units_sold_14d,
    0 AS brand_halo_units_sold_14d
  FROM
    sponsored_ads_traffic
)
SELECT
  advertiser,
  campaign,
  SUM(impressions) AS impressions,
  SUM(clicks) AS clicks,
  SUM(total_purchases_7d) AS total_purchases_7d,
  SUM(total_purchases_14d) AS total_purchases_14d,
  SUM(purchases_14d) AS purchases_14d,
  SUM(total_units_sold_14d) AS total_units_sold_14d,
  SUM(brand_halo_units_sold_14d) AS brand_halo_units_sold_14d,
  SUM(total_product_sales_14d) AS total_product_sales_14d
FROM
  traffic_and_conversion_events
GROUP BY
  advertiser,
  campaign
```
