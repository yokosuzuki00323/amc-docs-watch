# AMC data retention | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/datasources/data-retention

# AMC data retention

Was this page helpful?Amazon Marketing Cloud (AMC) instances accumulate advertising events on a rolling basis and retain the most recent event\-level data. Retention ranges from 13 months to 5 years, and it varies by data view, as shown in the following table.

Extended data retention allows eligible traffic data views to retain up to 5 years of history. It is activated automatically for all instances, with no request required. Instances have been backfilled so that most tables contain data back to June 2023\. Instances continue to accumulate data until they reach a maximum of 5 years; after that, they contain a rolling 5\-year window. Some data views are excluded from extended retention and remain at 13 months or follow a different schedule. Refer to the table for the retention window of each data view.

For guidance on writing efficient queries over longer time windows, refer to [Optimize AMC SQL queries](/API/docs/en-us/guides/amazon-marketing-cloud/amc-sql/how-to-opt-amc-sql-queries).

## Retention by data view

| Measurement Tables | Audience Tables | Retention |
| --- | --- | --- |
| `dsp_impressions`, `dsp_impressions_by_matched_segments`, `dsp_impressions_by_user_segments` | `dsp_impressions_for_audiences`, `dsp_impressions_by_matched_segments_for_audiences`, `dsp_impressions_by_user_segments_for_audiences` | backfilled from June 2023, accumulating up to 5 years† |
| `dsp_clicks` | `dsp_clicks_for_audiences` | backfilled from June 2023, accumulating up to 5 years† |
| `dsp_views` | `dsp_views_for_audiences` | backfilled from June 2023, accumulating up to 5 years† |
| `dsp_video_events_feed` | `dsp_video_events_feed_for_audiences` | backfilled from June 2023, accumulating up to 5 years† |
| `conversions`, `conversions_with_relevance` | `conversions_for_audiences`, `conversions_with_relevance_for_audiences` | backfilled from June 2023, accumulating up to 5 years† |
| `amazon_attributed_events_by_conversion_time`, `amazon_attributed_events_by_traffic_time` | `amazon_attributed_events_by_traffic_time_for_audiences` | backfilled from June 2023, accumulating up to 5 years† |
| `sponsored_ads_traffic` | `sponsored_ads_traffic_for_audiences` | backfilled from June 2023, accumulating up to 5 years† |
| `amazon_live_traffic` | `amazon_live_traffic_for_audiences` | backfilled from June 2023, accumulating up to 5 years† |
| `conversions_all` | `conversions_all_for_audiences` | backfilled from June 2023, accumulating up to 5 years† |
| `audience_segments*`, `segment_metadata` | `segment_metadata_for_audiences` | 13 months |
| `amazon_your_garage_all` | `amazon_your_garage_all_for_audiences` | 5 years† for non\-EU; 13 months for EU |
| `amazon_brand_store_page_views(_non_endemic)`, `amazon_brand_store_engagement_events(_non_endemic)` | `amazon_brand_store_page_views(_non_endemic)_for_audiences`, `amazon_brand_store_engagement_events(_non_endemic)_for_audiences` | 13 months |
| `amazon_retail_purchases` | `amazon_retail_purchases_for_audiences` | up to 5 years† |
| `amazon_pvc_enrollments`, `amazon_pvc_streaming_events_feed` | `amazon_pvc_enrollments_for_audiences`, `amazon_pvc_streaming_events_feed_for_audiences` | 13 months |
| `pv_streaming_events_feed` | `pv_streaming_events_feed_for_audiences` | 13 months |
| `experian_vehicle_purchases` | No associated audience table | 13 months |

† Backfilled so that most tables contain data back to June 2023\. Instances continue to accumulate data until they reach the 5\-year maximum, and then contain a rolling 5\-year window.
