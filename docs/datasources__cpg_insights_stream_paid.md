# NCS table | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/datasources/cpg_insights_stream_paid

# NC Solutions (NCS) CPG Insights Stream

Was this page helpful?**Analytics table:**

* `ncs_cpg_insights_stream`

**Audience table:**

* `ncs_cpg_insights_stream_for_audiences`

 Note Although you can use the audience view without a subscription, a CPM fee of $2 is applied on activation of the audience in Amazon DSP. Note NCS audience tables are not supported for Lookalike audience creation, or for audience activation in sponsored ads.NC Solutions (NCS) CPG Insights Stream provides offline modeled transactions at the household level, representing the total US population of 127MM\+ households. This data is derived by NCS by applying advanced machine learning models that utilize seed dataset comprising over 2\.7 trillion observed transaction records representing 98 million\+ US households. These records are collected from over 20\+ major national and regional CPG retailers across 56K\+ retail locations, and are combined with robust household\-level information from Nielsen to identify shopping patterns and similarities across households.

With NCS CPG Insights Stream, you can bring granular offline retail sales data into AMC. It allows you to holistically measure the impact of your online media, not just on driving online purchases but also on driving offline purchases. You can then use these insights to inform campaign and channel optimization strategies.

| Column Name | Data Type | Column Type | Column Description | Aggregation thresholds |
| --- | --- | --- | --- | --- |
| `brand` | `STRING` | `DIMENSION` | NCS syndicated brand name | `LOW` |
| `category` | `STRING` | `DIMENSION` | NCS syndicated product category name | `LOW` |
| `department` | `STRING` | `DIMENSION` | NCS syndicated department name | `LOW` |
| `household_purchase_id` | `STRING` | `DIMENSION` | Unique ID for the household purchase event, can be used to count distinct household purchases. | `VERY_HIGH` |
| `ncs_household_id` | `STRING` | `DIMENSION` | NCS household ID | `VERY_HIGH` |
| `no_3p_trackers` | `BOOLEAN` | `DIMENSION` | Is this item not allowed to use 3P tracking. | `NONE` |
| `product_category` | `STRING` | `DIMENSION` | NCS syndicated subscription resource object; associated with the `department`, `super_category` and `category` attributes | `LOW` |
| `purchase_dollar_amount` | `DecimalDataType(precision=38, scale=2)` | `METRIC` | US Dollar amount of products purchased | `LOW` |
| `purchase_quantity` | `INTEGER` | `METRIC` | Quantity of products purchased | `LOW` |
| `sub_brand` | `STRING` | `DIMENSION` | NCS syndicated sub brand name | `LOW` |
| `super_category` | `STRING` | `DIMENSION` | NCS syndicated super product category name | `LOW` |
| `user_id` | `STRING` | `DIMENSION` | User ID | `VERY_HIGH` |
| `user_id_type` | `STRING` | `DIMENSION` | Type of user ID | `LOW` |
| `week_end_dt` | `DATE` | `DIMENSION` | Week end date. Datestamp of last day included in the weekly transaction file. Datestamps will always be the Saturday of each week and represents purchases over the last 7 full days; Sunday\-Saturday. | `LOW` |
