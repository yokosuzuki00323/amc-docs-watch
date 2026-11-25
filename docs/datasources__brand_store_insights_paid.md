# Brand store insights | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/datasources/brand_store_insights_paid

# Amazon Brand Store insights tables

Was this page helpful?**Analytics tables:**

* `amazon_brand_store_page_views(_non_endemic)`
* `amazon_brand_store_engagement_events(_non_endemic)`

**Audiences tables:**

* `amazon_brand_store_page_views_for_audiences(_non_endemic)`
* `amazon_brand_store_engagement_events_for_audiences(_non_endemic)`

Amazon Brand Store insights is a collection of two AMC datasets that represent Brand Store page renders and interactions. Amazon Brand Store insights is a standalone AMC Paid Features resource that is available for trial and subscription enrollments within the AMC Paid Features suite of insight expansion options, powered by Amazon Ads.

The Amazon Brand Store insights resource is available to both endemic and non\-endemic advertisers that operate AMC instances within the supported AMC Paid Features account marketplaces (US, CA, JP, AU, FR, IT, ES, UK, DE, MX, BR, NL, SE, PL, BE, AE, SA, TR, EG, IE, ZA, NG, SG, IN).

 Note Starting June 1, 2026, you can query this dataset at no cost through December 31, 2026 in every region where it is available. If you already have an active subscription, it will automatically convert to zero dollars. For more details, refer to [Amazon 1P signals available at no cost](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/paid_features_overview#amazon-1p-signals-available-at-no-cost).## amazon\_brand\_store\_page\_views (\_non\_endemic)

Brand Store page view events, including dwell time. Events are at the Store page\-level. The `visit_id` or `session_id` columns can be converted to metrics via `COUNT()` or `COUNT(distinct )` SQL aggregate functions.

| Field Category | Name | Data Type | Metric / Dimension | Description | Aggregation Threshold |
| --- | --- | --- | --- | --- | --- |
| Brand Store insights | `advertiser_id` | `LONG` | Dimension | Advertiser ID. | LOW |
| Brand Store insights | `channel` | `STRING` | Dimension | Channel tag ID, referenced as query string name. | LOW |
| Brand Store insights | `device_type` | `STRING` | Dimension | Device type that viewed the store. | MEDIUM |
| Brand Store insights | `dwell_time` | `DECIMAL` | Dimension | Dwell time of page view (in seconds). | LOW |
| Brand Store insights | `event_date_utc` | `DATE` | Dimension | Date of event in UTC. | LOW |
| Brand Store insights | `event_dt_utc` | `TIMESTAMP` | Dimension | Timestamp of event in UTC. | LOW |
| Brand Store insights | `ingress_type` | `STRING` | Dimension | Enumerated list of store traffic source:0 \- uncategorized / default1 \- search2 \- detail page byline4 \- ads6 \- store recommendations7 through 11 \- experimentation | MEDIUM |
| Brand Store insights | `marketplace_id` | `INTEGER` | Dimension | Marketplace ID of the store. | INTERNAL |
| Brand Store insights | `page_id` | `STRING` | Dimension | Store page ID. | LOW |
| Brand Store insights | `page_title` | `STRING` | Dimension | Title of the page. | LOW |
| Brand Store insights | `reference_id` | `STRING` | Dimension | Identifier for the ad campaign that is associated with the Brand Store page visit, associated with `ingress_type` \= 4\. | LOW |
| Brand Store insights | `referrer_domain` | `STRING` | Dimension | HTML referrer domain from which user arrived at page from, for example google.com (external) or amazon.com (internal). | LOW |
| Brand Store insights | `session_id` | `STRING` | Dimension | Store session ID. | VERY HIGH |
| Brand Store insights | `store_name` | `STRING` | Dimension | Name of the store set by the store owner. | LOW |
| Brand Store insights | `user_id` | `STRING` | Dimension | User ID that performed the event. | VERY HIGH |
| Brand Store insights | `user_id_type` | `STRING` | Dimension | Type of User ID. | LOW |
| Brand Store insights | `visit_id` | `STRING` | Dimension | Store visit ID. | VERY HIGH |
| Brand Store insights | `no_3p_trackers` | `BOOLEAN` | Dimension | Indicates whether this item is not allowed to use 3P tracking. | NONE |

## amazon\_brand\_store\_engagement\_events (\_non\_endemic)

Brand Store engagement events. Provides Brand Store web engagement metrics including page views and clicks. Events are interaction based and presented at the Store widget\-level. The `visit_id` or `session_id` columns can be converted to metrics via `COUNT()` or `COUNT(distinct )` SQL aggregate functions.

| Field Category | Name | Data Type | Metric / Dimension | Description | Aggregation Threshold |
| --- | --- | --- | --- | --- | --- |
| Brand Store insights | `advertiser_id` | `LONG` | Dimension | Advertiser ID. | LOW |
| Brand Store insights | `asin` | `STRING` | Dimension | Amazon Standard Identification Number (`ASIN`). | LOW |
| Brand Store insights | `channel` | `STRING` | Dimension | Channel tag ID, referenced as query string name. | LOW |
| Brand Store insights | `device_type` | `STRING` | Dimension | Device type that viewed the store. | MEDIUM |
| Brand Store insights | `event_date_utc` | `DATE` | Dimension | Date of event in UTC. | LOW |
| Brand Store insights | `event_dt_utc` | `TIMESTAMP` | Dimension | Timestamp of event in UTC. | LOW |
| Brand Store insights | `event_sub_type` | `STRING` | Dimension | Sub\-type of event \- refer to schema for values. | LOW |
| Brand Store insights | `event_type` | `STRING` | Dimension | Type of event \- refer to schema for values. | LOW |
| Brand Store insights | `ingress_type` | `STRING` | Dimension | Enumerated list of store traffic source:0 \- uncategorized / default1 \- search2 \- detail page byline4 \- ads6 \- store recommendations7 through 11 \- experimentation |  |
| Brand Store insights | `marketplace_id` | `INTEGER` | Dimension | Marketplace ID of the store. | INTERNAL |
| Brand Store insights | `page_id` | `STRING` | Dimension | Store page ID. | LOW |
| Brand Store insights | `page_title` | `STRING` | Dimension | Title of the page. | LOW |
| Brand Store insights | `reference_id` | `STRING` | Dimension | Identifier for the ad campaign that is associated with the Brand Store page visit, associated with `ingress_type` \= 4\. | LOW |
| Brand Store insights | `referrer_domain` | `STRING` | Dimension | HTML referrer domain from which user arrived at page from, for example google.com (external) or amazon.com (internal). | LOW |
| Brand Store insights | `session_id` | `STRING` | Dimension | Store session ID. | VERY HIGH |
| Brand Store insights | `store_name` | `STRING` | Dimension | Name of the store set by the store owner. | LOW |
| Brand Store insights | `user_id` | `STRING` | Dimension | User ID that performed the event. | VERY HIGH |
| Brand Store insights | `user_id_type` | `STRING` | Dimension | Type of User ID. | LOW |
| Brand Store insights | `widget_sub_type` | `STRING` | Dimension | Sub\-type of widget \- refer to schema for values. | LOW |
| Brand Store insights | `widget_type` | `STRING` | Dimension | Type of widget \- refer to schema for values. | LOW |
| Brand Store insights | `no_3p_trackers` | `BOOLEAN` | Dimension | Indicates whether this item is not allowed to use 3P tracking. | NONE |
