# Amazon Prime Video Channel Insights | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/datasources/prime_video_channel_insights_paid

# Amazon Prime Video Channel Insights

Was this page helpful?**Analytics tables:**

* `amazon_pvc_enrollments`
* `amazon_pvc_streaming_events_feed`

**Audience tables:**

* `amazon_pvc_enrollments_for_audiences`
* `amazon_pvc_streaming_events_feed_for_audiences`

Amazon Prime Video Channel Insights is a collection of two AMC data views that represent Prime Video Channel subscriptions and streaming signals. Amazon Prime Video Channel Insights is a standalone AMC Paid Features resource that is available for trial and subscription enrollments within the AMC Paid Features suite of insight expansion options, powered by Amazon Ads. This resource is available to Amazon Advertisers that operate Prime Video Channels within the supported AMC Paid Features account marketplaces (US/CA/JP/AU/FR/IT/ES/UK/DE).

 Note Amazon Prime Video Channel Insights (PVCI) is a separate, distinct dataset from [Amazon Prime Video Insights](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/prime-video-insights-paid) (PVI). PVCI measures Prime Video Channel subscription and streaming signals; PVI measures Prime Video streaming/viewership signals more broadly. Note Starting June 1, 2026, you can query this dataset at no cost through December 31, 2026 in every region where it is available. If you already have an active subscription, it will automatically convert to zero dollars. For more details, refer to [Amazon 1P signals available at no cost](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/paid_features_overview#amazon-1p-signals-available-at-no-cost).## amazon\_pvc\_enrollments

Amazon Prime Video Channels enrollment records presented per benefit id. The `pv_subscription_id` column can be converted to metrics via `COUNT()` or `COUNT(DISTINCT)` SQL aggregate functions.

| Name | Data Type | Metric/Dimension | Description | Aggregation Threshold |
| --- | --- | --- | --- | --- |
| `marketplace_id` | `LONG` | `DIMENSION` | ID of the marketplace where the Amazon Prime Video Channel enrollment event occurred | `INTERNAL` |
| `marketplace_name` | `STRING` | `DIMENSION` | This is the marketplace associated with the Amazon Prime Video Channel record | `LOW` |
| `no_3p_trackers` | `BOOLEAN` | `DIMENSION` | Boolean value indicating whether the event can be used for audience creation that is third\-party tracking enabled (i.e. whether you can serve creative with third\-party tracking when running media against the audience). Third\-party tracking refers to measurement tags and pixels from external vendors that can be used to measure ad performance. Possible values for this field are: `true`, `false`. | `LOW` |
| `pv_benefit_id` | `STRING` | `DIMENSION` | Amazon Prime Video subscription benefit identifier | `INTERNAL` |
| `pv_benefit_name` | `STRING` | `DIMENSION` | Amazon Prime Video subscription benefit name | `LOW` |
| `pv_billing_type` | `STRING` | `DIMENSION` | Amazon Prime Video billing type for the enrollment record | `MEDIUM` |
| `pv_currency_code` | `STRING` | `DIMENSION` | Currency code for the PVC enrollment plan | `LOW` |
| `pv_duration_days` | `INTEGER` | `DIMENSION` | Duration in days for the PVC enrollment plan | `LOW` |
| `pv_duration_length` | `DECIMAL(38,18)` | `DIMENSION` | Duration length for the PVC enrollment plan | `LOW` |
| `pv_duration_units` | `STRING` | `DIMENSION` | Duration units for the PVC enrollment plan (e.g., MONTH, YEAR) | `LOW` |
| `pv_end_date` | `DATE` | `DIMENSION` | Interval\-specific end date associated with the PVC enrollment record | `LOW` |
| `pv_enrollment_status` | `STRING` | `DIMENSION` | Status for the PVC enrollment record | `LOW` |
| `pv_is_latest_record` | `BOOLEAN` | `DIMENSION` | Indicator of whether the PVC enrollment record is the most recent record within the table | `INTERNAL` |
| `pv_is_plan_conversion` | `BOOLEAN` | `DIMENSION` | Indicates whether the PVC enrollment record has converted from Free Trial to a subscription. This is often associated with a change in the billing type for the PVC subscription | `LOW` |
| `pv_is_plan_start` | `BOOLEAN` | `DIMENSION` | Indicates whether the PVC enrollment record is the start of an enrollment. This is often the opening of a free trial or the first subscription record for the PV subscription ID | `LOW` |
| `pv_is_promo` | `BOOLEAN` | `DIMENSION` | Indicator of whether the PVC enrollment record is associated with a promotional offer | `LOW` |
| `pv_offer_name` | `STRING` | `DIMENSION` | Amazon Prime Video subscription offer name | `HIGH` |
| `pv_plan_type_id` | `STRING` | `DIMENSION` | Amazon Prime Video plan type identifier | `INTERNAL` |
| `pv_start_date` | `DATE` | `DIMENSION` | Interval\-specific start date associated with the PVC enrollment record | `LOW` |
| `pv_sub_event_primary_key` | `STRING` | `DIMENSION` | Unique identifier for the PVC enrollment event | `INTERNAL` |
| `pv_subscription_id` | `STRING` | `DIMENSION` | Amazon Prime Video subscription id | `INTERNAL` |
| `pv_subscription_name` | `STRING` | `DIMENSION` | Amazon Prime Video subscription name | `LOW` |
| `pv_subscription_product_id` | `STRING` | `DIMENSION` | Amazon Prime Video subscription product identifier | `INTERNAL` |
| `pv_unit_price` | `DECIMAL` | `DIMENSION` | Unit price for the PVC enrollment record | `NONE` |
| `user_id` | `STRING` | `DIMENSION` | Pseudonymous identifier that connects user activity across different events. The field can contain ad user IDs (representing Amazon accounts), device IDs, or browser IDs. `NULL` values appear when Amazon Ads is unable to resolve an identifier for an event. The field has a `VERY_HIGH` aggregation threshold, meaning it cannot be included in final `SELECT` statements but can be used within Common Table Expressions (CTEs) for aggregation purposes like `COUNT(DISTINCT user_id)`. | `VERY_HIGH` |
| `user_id_type` | `STRING` | `DIMENSION` | Type of user ID value. AMC includes different types of user ID values, depending on whether the value represents a resolved Amazon account, a device, or a browser cookie. If Amazon Ads is unable to determine or provide an ID of any kind for an impression event, the `user_id` and `user_id_type` values for that record will be `NULL`. Possible values include: `adUserId`, `sisDeviceId`, `adBrowserId`, and `NULL`. | `LOW` |

## amazon\_pvc\_streaming\_events\_feed

Amazon Prime Video Channel Streaming and engagement events. Provides Amazon Prime Video Channel engagement metrics including content metadata, request context and duration. Events are session based and presented at the PVC benefit\-level. The `pv_session_id` columns can be converted to metrics via `COUNT()` or `COUNT(DISTINCT)` SQL aggregate functions.

| Name | Data Type | Metric/Dimension | Description | Aggregation Threshold |
| --- | --- | --- | --- | --- |
| `marketplace_id` | `LONG` | `DIMENSION` | Marketplace id of the event | `INTERNAL` |
| `marketplace_name` | `STRING` | `DIMENSION` | Marketplace name of the event | `LOW` |
| `no_3p_trackers` | `BOOLEAN` | `DIMENSION` | Boolean value indicating whether the event can be used for audience creation that is third\-party tracking enabled (i.e. whether you can serve creative with third\-party tracking when running media against the audience). Third\-party tracking refers to measurement tags and pixels from external vendors that can be used to measure ad performance. Possible values for this field are: `true`, `false`. | `LOW` |
| `pv_access_type` | `STRING` | `DIMENSION` | Content access type e.g. free, prime subscription, rental, purchase | `LOW` |
| `pv_gti_cast` | `ARRAY` | `DIMENSION` | Content cast members | `LOW` |
| `pv_content_details` | `STRING` | `DIMENSION` | Additional detail on content | `LOW` |
| `pv_gti_content_entity_type` | `STRING` | `DIMENSION` | Content entity (sub) type e.g. Short Film, Educational | `LOW` |
| `pv_gti_content_rating` | `STRING` | `DIMENSION` | Content rating | `LOW` |
| `pv_gti_content_type` | `STRING` | `DIMENSION` | Content type e.g. TV Episode, Movie, Promotion | `LOW` |
| `pv_gti_director` | `ARRAY` | `DIMENSION` | Content directors | `LOW` |
| `pv_gti_episode` | `STRING` | `DIMENSION` | Series episode | `LOW` |
| `pv_gti_event_context` | `STRING` | `DIMENSION` | Content event context | `LOW` |
| `pv_gti_event_item` | `STRING` | `DIMENSION` | Content event item | `LOW` |
| `pv_gti_event_league` | `STRING` | `DIMENSION` | Content event league | `LOW` |
| `pv_gti_event_name` | `STRING` | `DIMENSION` | Content event name | `LOW` |
| `pv_gti_event_sport` | `STRING` | `DIMENSION` | Content event sport | `LOW` |
| `pv_gti_genre` | `ARRAY` | `DIMENSION` | Content genre | `LOW` |
| `pv_gti_is_live` | `BOOLEAN` | `DIMENSION` | Content is live boolean | `LOW` |
| `pv_gti_release_date` | `DATE` | `DIMENSION` | Content release date | `LOW` |
| `pv_gti_season` | `STRING` | `DIMENSION` | Series season | `LOW` |
| `pv_gti_series_or_movie_name` | `STRING` | `DIMENSION` | Series or movie name | `LOW` |
| `pv_gti_studio` | `STRING` | `DIMENSION` | Content studio | `LOW` |
| `pv_gti_title_name` | `STRING` | `DIMENSION` | Content title e.g. episode name | `LOW` |
| `pv_is_adfree` | `BOOLEAN` | `DIMENSION` | Is the content ad free | `LOW` |
| `pv_is_avod` | `BOOLEAN` | `DIMENSION` | Is advertiser\-supported VOD boolean | `LOW` |
| `pv_is_channels` | `BOOLEAN` | `DIMENSION` | Is channel boolean | `LOW` |
| `pv_is_svod` | `BOOLEAN` | `DIMENSION` | Is subscription VOD boolean | `LOW` |
| `pv_is_user_initiated` | `BOOLEAN` | `DIMENSION` | User\-initiated content or auto\-play content | `LOW` |
| `pv_material_type` | `STRING` | `DIMENSION` | Video material type e.g. full, live, promo, trailer | `LOW` |
| `pv_offer_group` | `STRING` | `DIMENSION` | Content offer group e.g. free, prime, rental, purchase | `LOW` |
| `pv_profile_type` | `STRING` | `DIMENSION` | Type of profile associated with the content | `LOW` |
| `pv_playback_date_utc` | `DATE` | `DIMENSION` | Date of the event | `LOW` |
| `pv_playback_dt_utc` | `TIMESTAMP` | `DIMENSION` | Timestamp of the event | `MEDIUM` |
| `pv_seconds_viewed` | `DECIMAL` | `METRIC` | The seconds of view time associated with a streaming event | `MEDIUM` |
| `pv_session_id` | `STRING` | `DIMENSION` | Session ID of the event | `VERY_HIGH` |
| `pv_stream_type` | `STRING` | `DIMENSION` | Type of stream content e.g. linear tv, live\_event, VOD | `LOW` |
| `pv_streaming_asin` | `STRING` | `DIMENSION` | Amazon Standard Identification Number (`ASIN`) | `LOW` |
| `pv_streaming_geo_dma` | `STRING` | `DIMENSION` | DMA code | `LOW` |
| `pv_streaming_geo_country` | `STRING` | `DIMENSION` | Country accessing the event | `LOW` |
| `pv_streaming_geo_city` | `STRING` | `DIMENSION` | City accessing the event | `LOW` |
| `pv_streaming_gti` | `STRING` | `DIMENSION` | Global title information | `LOW` |
| `pv_streaming_language` | `STRING` | `DIMENSION` | Language of the event | `LOW` |
| `user_id` | `STRING` | `DIMENSION` | Pseudonymous identifier that connects user activity across different events. The field can contain ad user IDs (representing Amazon accounts), device IDs, or browser IDs. `NULL` values appear when Amazon Ads is unable to resolve an identifier for an event. The field has a `VERY_HIGH` aggregation threshold, meaning it cannot be included in final `SELECT` statements but can be used within Common Table Expressions (CTEs) for aggregation purposes like `COUNT(DISTINCT user_id)`. | `VERY_HIGH` |
| `user_id_type` | `STRING` | `DIMENSION` | Type of user ID value. AMC includes different types of user ID values, depending on whether the value represents a resolved Amazon account, a device, or a browser cookie. If Amazon Ads is unable to determine or provide an ID of any kind for an impression event, the `user_id` and `user_id_type` values for that record will be `NULL`. Possible values include: `adUserId`, `sisDeviceId`, `adBrowserId`, and `NULL`. | `LOW` |
