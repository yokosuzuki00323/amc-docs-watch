# Amazon Prime Video Insights | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/datasources/prime-video-insights-paid

# Amazon Prime Video Insights

Was this page helpful?**Analytics table:**

* `pv_streaming_events_feed`

**Audience table:**

* `pv_streaming_events_feed_for_audiences`

## Overview

Amazon Prime Video is a subscription\-based video on demand streaming and rental service that Amazon bundles within the Amazon Prime subscription. The service features a comprehensive content library including ad\-supported and ad\-free content, Live TV, Sports on Prime, and both first and third\-party content available for rental or subscription. This dataset allows advertisers to analyze content engagement patterns across Prime Video for their customers.

Amazon Prime Video Insights (PVI) helps advertisers better understand the entertainment preferences of their customers and how these intersect with other customer behaviors. By combining Prime Video viewership insights with other AMC signals, advertisers can develop better campaign strategies to reach the right audience, measure the relationship between viewing behavior and purchase patterns, and create more relevant audience segments. Additionally, these signals allow advertisers to understand the overlap between their customer base and Prime Video viewers, providing valuable insight into new audiences on Prime Video, especially for non\-endemic advertisers who don't sell on Amazon. Advertisers can use PVI alongside Amazon DSP traffic events, sponsored ads event\-level signals, conversion events, and advertiser\-uploaded signals to conduct custom attribution for subscriptions, re\-engagement campaigns, and audience overlap analysis.

 Note Starting June 1, 2026, you can query this dataset at no cost through December 31, 2026 in every region where it is available. If you already have an active subscription, it will automatically convert to zero dollars. For more details, refer to [Amazon 1P signals available at no cost](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/paid_features_overview#amazon-1p-signals-available-at-no-cost). Note Prime Video Insights (PVI) is a separate, distinct dataset from [Amazon Prime Video Channel Insights](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/prime_video_channel_insights_paid) (PVCI). PVI measures streaming/viewership signals across Prime Video; PVCI measures Prime Video Channel subscription and streaming signals.## Basic information

**Lookback:** The PVI lookback window is 13 months.

**Availability:** AMC accounts/instances associated with the US, CA, JP, AU, FR, IT, ES, UK, DE, MX, BR, NL, SE, PL, BE, AE, SA, TR, EG, IE, ZA, NG, SG, IN marketplaces

**Eligibility:** All AMC advertisers and instances within the eligible marketplaces above. Data coverage is limited to users an advertiser has reached through an upstream data join with ad traffic tables.

**Contains signals from:** US, CA, JP, AU, FR, IT, ES, UK, DE, MX, BR, NL, SE, PL, BE, AE, SA, TR, EG, IE, ZA, NG, SG, IN marketplaces

For eligible advertisers and instances, the associated audience table can be used for AMC audience creation without a Paid Feature subscription:

* `pv_streaming_events_feed_for_audiences`

## `pv_streaming_events_feed`

| Name | Data Type | Metric/Dimension | Description | Aggregation Threshold |
| --- | --- | --- | --- | --- |
| `marketplace_id` | `LONG` | `DIMENSION` | Marketplace ID of the event | `INTERNAL` |
| `marketplace_name` | `STRING` | `DIMENSION` | Marketplace name of the event | `LOW` |
| `no_3p_trackers` | `BOOLEAN` | `DIMENSION` | Boolean value indicating whether the event can be used for audience creation that is third\-party tracking enabled (i.e. whether you can serve creative with third\-party tracking when running media against the audience). Third\-party tracking refers to measurement tags and pixels from external vendors that can be used to measure ad performance. Possible values for this field are: `true`, `false`. | `LOW` |
| `pv_access_type` | `STRING` | `DIMENSION` | Content access type e.g. free, Prime subscription, rental, purchase | `LOW` |
| `pv_content_details` | `STRING` | `DIMENSION` | Additional detail on content | `LOW` |
| `pv_gti_cast` | `ARRAY` | `DIMENSION` | Content cast members | `LOW` |
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
| `pv_is_adfree` | `BOOLEAN` | `DIMENSION` | Ad free content boolean | `LOW` |
| `pv_is_avod` | `BOOLEAN` | `DIMENSION` | Is advertiser\-supported VOD boolean | `LOW` |
| `pv_is_channels` | `BOOLEAN` | `DIMENSION` | Is channel boolean | `LOW` |
| `pv_is_svod` | `BOOLEAN` | `DIMENSION` | Is subscription VOD boolean | `LOW` |
| `pv_is_user_initiated` | `BOOLEAN` | `DIMENSION` | User\-initiated content or auto\-play content | `LOW` |
| `pv_material_type` | `STRING` | `DIMENSION` | Video material type e.g. full, live, promo, trailer | `LOW` |
| `pv_offer_group` | `STRING` | `DIMENSION` | Content offer group e.g. free, prime, rental, purchase | `LOW` |
| `pv_playback_date_utc` | `DATE` | `DIMENSION` | Date of the event | `LOW` |
| `pv_profile_type` | `STRING` | `DIMENSION` | Type of profile associated with the content | `LOW` |
| `pv_playback_dt_utc` | `TIMESTAMP` | `DIMENSION` | Timestamp of the event | `MEDIUM` |
| `pv_seconds_viewed` | `DECIMAL` | `METRIC` | The seconds of view time associated with a streaming event | `MEDIUM` |
| `pv_session_id` | `STRING` | `DIMENSION` | Session ID of the event | `VERY_HIGH` |
| `pv_stream_type` | `STRING` | `DIMENSION` | Type of stream content e.g. linear tv, live\_event, VOD | `LOW` |
| `pv_streaming_asin` | `STRING` | `DIMENSION` | Amazon Standard Identification Number (`ASIN`) | `LOW` |
| `pv_streaming_geo_city` | `STRING` | `DIMENSION` | City accessing the event | `LOW` |
| `pv_streaming_geo_country` | `STRING` | `DIMENSION` | Country accessing the event | `LOW` |
| `pv_streaming_geo_dma` | `STRING` | `DIMENSION` | DMA code | `LOW` |
| `pv_streaming_gti` | `STRING` | `DIMENSION` | Global title information | `LOW` |
| `pv_streaming_language` | `STRING` | `DIMENSION` | Language of the event | `LOW` |
| `user_id` | `STRING` | `DIMENSION` | Pseudonymous identifier that connects user activity across different events. The field can contain ad user IDs (representing Amazon accounts), device IDs, or browser IDs. `NULL` values appear when Amazon Ads is unable to resolve an identifier for an event. The field has a `VERY_HIGH` aggregation threshold, meaning it cannot be included in final `SELECT` statements but can be used within Common Table Expressions (CTEs) for aggregation purposes like `COUNT(DISTINCT user_id)`. | `VERY_HIGH` |
| `user_id_type` | `STRING` | `DIMENSION` | Type of user ID value. AMC includes different types of user ID values, depending on whether the value represents a resolved Amazon account, a device, or a browser cookie. If Amazon Ads is unable to determine or provide an ID of any kind for an impression event, the `user_id` and `user_id_type` values for that record will be `NULL`. Possible values include: `adUserId`, `sisDeviceId`, `adBrowserId`, and `NULL`. | `LOW` |
