# Amazon your garage | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/datasources/amazon_your_garage_paid

# Amazon Your Garage tables

Was this page helpful?**Analytics table:**

* `amazon_your_garage_all`

**Audiences table:**

* `amazon_your_garage_all_for_audiences`

Amazon Your Garage is a virtual vehicle repository which allows customers to add their vehicle make and model and quickly locate parts and accessories that fit their saved vehicles. The AMC Amazon Your Garage (AYG) dataset allows you to tap into those user\-to\-vehicle association signals. When you enroll in Amazon Your Garage, you will have access to the `amazon_your_garage_all` dataset containing signals such as vehicle type, make, or engine type, which are updated daily with the most recent user\-to\-vehicle associations.

The data "snapshot" will be the most\-recent available user\-to\-vehicle association, refreshed and published into AMC daily. Advertisers can use Amazon Your Garage signals alongside Amazon DSP traffic events, sponsored ads event\-level signals, Paid feature subscriptions, and advertiser uploaded signals in order to conduct saved vehicle segment analysis for planning, measurement, and activation purposes.

Prior to 10/17/2025, the AMC Amazon Your Garage dataset (`amazon_your_garage`) was available in the NA region only. After 10/17/2025, the Amazon Your Garage dataset was expanded to also include EU and FE regions. The expanded tables are titled `amazon_your_garage_all` and `amazon_your_garage_all_for_audiences`. For more information about eligibility and availability, refer to [Paid features overview](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/paid_features_overview).

 Note Starting June 1, 2026, you can query this dataset at no cost through December 31, 2026 in every region where it is available. If you already have an active subscription, it will automatically convert to zero dollars. For more details, refer to [Amazon 1P signals available at no cost](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/paid_features_overview#amazon-1p-signals-available-at-no-cost). Note The `amazon_your_garage` and `amazon_your_garage_for_audiences` tables will be deprecated on December 12, 2025\.

| Column name | Data type | Metric/dimension | Description | Aggregation threshold |
| --- | --- | --- | --- | --- |
| `creation_date` | `DATE` | `DIMENSION` | Creation date of the record | `LOW` |
| `garage_bodystyle` | `STRING` | `DIMENSION` | Vehicle body style attribute | `LOW` |
| `garage_brakes` | `STRING` | `DIMENSION` | Vehicle brakes attribute | `LOW` |
| `garage_drivetype` | `STRING` | `DIMENSION` | Vehicle drive type attribute | `LOW` |
| `garage_engine` | `STRING` | `DIMENSION` | Vehicle engine attribute | `LOW` |
| `garage_engine_output_hp` | `FLOAT` | `DIMENSION` | Engine output in horsepower | `LOW` |
| `garage_engine_output_kw` | `FLOAT` | `DIMENSION` | Engine output in kilowatts | `LOW` |
| `garage_make` | `STRING` | `DIMENSION` | Vehicle make attribute | `LOW` |
| `garage_model` | `STRING` | `DIMENSION` | Vehicle model attribute | `LOW` |
| `garage_springtypes` | `STRING` | `DIMENSION` | Spring type attribute | `LOW` |
| `garage_submodel` | `LONG` | `DIMENSION` | Vehicle submodel identifier | `LOW` |
| `garage_transmission` | `STRING` | `DIMENSION` | Vehicle transmission attribute | `LOW` |
| `garage_variant` | `STRING` | `DIMENSION` | Vehicle variant name attribute | `LOW` |
| `garage_year` | `DATE` | `DIMENSION` | Vehicle year attribute | `LOW` |
| `garage_year_range` | `DATE` | `DIMENSION` | Vehicle model year range | `LOW` |
| `last_accessed_date` | `DATE` | `DIMENSION` | Last accessed date for a customer invoked interaction with Amazon Garage record | `LOW` |
| `marketplace_name` | `STRING` | `DIMENSION` | This is the marketplace associated with the Amazon Garage record (Note: not the AMC Paid Feature marketplace). | `LOW` |
| `no_3p_trackers` | `BOOLEAN` | `DIMENSION` | Is this item not allowed to use 3P tracking | `NONE` |
| `region` | `STRING` | `DIMENSION` | Region associated with the Amazon marketplace. | `LOW` |
| `status` | `STRING` | `DIMENSION` | Status of record | `LOW` |
| `update_date` | `DATE` | `DIMENSION` | Update date for the most recent garage record edit | `LOW` |
| `user_id` | `STRING` | `DIMENSION` | User ID of the customer | `VERY_HIGH` |
| `vehicle_type` | `STRING` | `DIMENSION` | Vehicle type attribute | `LOW` |
