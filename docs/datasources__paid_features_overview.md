# Paid features overview | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/datasources/paid_features_overview

# Paid features overview

Was this page helpful?## What are AMC Paid features?

AMC Paid Features are a set of enhanced datasets that provide more expanded insights into customer behavior and advertising campaign performance than the standard AMC features. For analytics queries, these features require a monthly subscription and unlock access to a variety of signals, allowing for more granular analysis and targeted campaigns. Depending on availability and eligibility, you can leverage many of the associated paid features audience tables without a subscription.

## Amazon 1P signals available at no cost

Starting June 1, 2026, all Amazon 1P signals covered under AMC Paid Features—Amazon Insights, Amazon Retail Purchases, Prime Video Insights, Prime Video Channel Insights, Amazon Your Garage, and Brand Store Insights—will be available to query at no cost through December 31, 2026 in all regions where [AMC Paid Features are available](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/paid_features_overview#paid-features-availability-and-eligibility).

Eligible advertisers can subscribe through the AMC Paid Features page and run queries utilizing these signals at no additional cost, unlocking advanced measurement use cases. If you already have an active subscription, no action is needed — your subscription will automatically convert to zero dollars.

 Note 3P paid features (e.g., Experian Auto Vehicle Purchase Insights) will continue to require a subscription fee. The NCS paid feature has been discontinued and is no longer available. For details on all available paid features, refer to the AMC Paid Features page in the AMC UI.## Paid features availability and eligibility

Which Paid features datasets that are available to you depend on:

* The availability of the feature in certain regions and marketplaces. Availability varies per feature. For the full list of supported markets, refer to each dataset's availability details below.
* The eligibility requirements of each paid feature (for example, Prime Video Channel insights is only available for Amazon advertisers that operate Prime Video Channels).

### Analytics

For analytics datasets, before you can enroll in a paid features subscription or free trial, the paid feature must be available for the region or marketplace associated with your account and your instance must meet certain eligibility requirements.

If the paid feature is not available for your region or marketplace, you will not see it on the Paid feature tab. If it is available, but you are not eligible, you will not be able to click Subscribe on the Paid features tab.

### Audiences

For audience datasets, if the Paid feature is available in your region or marketplace and your instance is eligible, the audience table will be automatically available in your instance. In this case, you do not have to subscribe to the Paid feature to start generating audiences.

If it is not available or you are not eligible, you will not see the audience table in your instance and you will not be able to subscribe to that paid feature.

### Signal availability

The signals included in the paid features dataset may vary based on region or marketplace. For example, audiences created with the Amazon Retail Purchases (ARP) dataset will not include signals from the EU region or UK marketplace. These signals, however, are available for measurement queries using ARP.

### AMC paid features billing

AMC Paid feature subscription enrollments are facilitated through the eligible billing account types listed below. The billing accounts are inferred based on the advertiser resources that are associated with the AMC instance object.

* Sponsored Ads entity billing accounts
* DSP Self\-Service entity billing accounts
* Amazon Advertising Incentive Center Measurement Funds

### How to subscribe to AMC Paid features

To subscribe to an AMC Paid feature:

1. Log into the Amazon advertising console and open the AMC user interface.
2. Go to the **Paid features** tab to view a listing of all paid features that are available to you.
3. If you are eligible to subscribe, click **See options** to view additional details, such as price, and to select a billing account.
4. Read the Amazon Marketing Cloud terms and conditions and click the checkbox to accept the terms and conditions.
5. When you are ready, click **Subscribe**. All users associated with this instance will now have access to the subscribed paid feature.

## Flexible Shopping Insights (FSI) as a part of Amazon Insights

**Availability:** AMC accounts associated with US, CA, JP, AU, FR, IT, ES, UK, DE, MX, BR, NL, SE, PL, BE, AE, SA, TR, EG, IE, ZA, NG, SG, IN marketplaces

**Eligibility:** At least one sponsored ads account associated with your AMC instance must belong to a seller (Seller Central) or to a vendor that is a registered brand owner in Amazon Brand Registry. Instances that only have Amazon DSP advertisers, or only have vendors that are not registered brand owners, are not eligible.

**Contains signals from:** All available marketplaces

Flexible Shopping Insights (FSI) is a part of Amazon Insights subscription, and enables advertisers to generate combined, aggregated, and anonymized advertising and shopping insights for brands and products advertised through Amazon Ads

* `conversions_all`

For eligible advertisers and instances, the associated audience table can be used for AMC audience creation without a Paid feature subscription:

* `conversions_all_for_audiences`

Refer to [conversions\_all](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/conversions_all_paid).

## Audience Segment Insights (ASI) as a part of Amazon Insights

**Availability:** AMC accounts associated with the US, CA, JP, AU, FR, IT, ES, UK, DE, MX, BR, NL, SE, PL, BE, AE, SA, TR, EG, IE, ZA, NG, SG, IN marketplaces

**Eligibility:** Any AMC advertisers

**Contains signals from:** All available marketplaces

Amazon Audience Segment Insights enable advertisers to conduct user\-to\-segment analysis within Amazon Marketing Cloud (AMC) for all Amazon Ads customers across all datasets published into AMC as well as segment\-level analysis for advertiser uploaded datasets.

Amazon Audience Segment Insights is a part of the Amazon Insights subscription for advertisers that sell on Amazon (endemic). Alternatively, Amazon Audience Segment Insights is available for advertisers that do not sell on Amazon (non\-endemic) via a la carte subscription.

* `audience_segments_[amer|apac|eu]_inmarket`
* `audience_segments_[amer|apac|eu]_inmarket_snapshot`
* `audience_segments_[amer|apac|eu]_lifestyle`
* `audience_segments_[amer|apac|eu]_lifestyle_snapshot`
* `segment_metadata`

For eligible advertisers and instances, the associated audience tables can be used for AMC audience creation without a Paid feature subscription:

* `audience_segments_[amer|apac|eu]_inmarket_for_audiences`
* `audience_segments_[amer|apac|eu]_inmarket_snapshot_for_audiences`
* `audience_segments_[amer|apac|eu]_lifestyle_for_audiences`
* `audience_segments_[amer|apac|eu]_lifestyle_snapshot_for_audiences`
* `segment_metadata_for_audiences`

Refer to [Amazon Audience Segment Insights](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/audience_segment_membership_paid).

## Amazon your garage

**Availability:** US, JP, CA, AU, UK, DE, FR, IT, ES marketplaces

**Eligibility:** Any AMC advertisers

**Contains signals from:** US, CA, UK, DE, FR, IT, ES, NL, PL, SE, JP, and AU Amazon websites

Additionally, the Amazon Your Garage paid feature provides user\-to\-vehicle association details that describe vehicle type, the make and model of the vehicle, as well as detailed vehicle configuration attributes expressed in the context of an AMC `user_id`.

* `amazon_your_garage_all`

For eligible advertisers and instances, the associated audience table can be used for AMC audience creation without a Paid feature subscription:

* `amazon_your_garage_all_for_audiences`

Refer to [Amazon your garage](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/amazon_your_garage_paid).

## Amazon Brand Store insights (BSI)

**Availability:** AMC accounts associated with US, CA, JP, AU, FR, IT, ES, UK, DE, MX, BR, NL, SE, PL, BE, AE, SA, TR, EG, IE, ZA, NG, SG, IN marketplaces

**Eligibility:** Advertisers with at least one active brand store

**Contains signals from:** US, CA, JP, AU, FR, IT, ES, UK, DE, MX, BR, NL, SE, PL, BE, AE, SA, TR, EG, IE, ZA, NG, SG, IN marketplaces

Amazon Brand Store Insights (BSI) is an AMC paid feature that allows advertisers to tap into page visit, dwell time, and interaction signals from Amazon Brand Stores.

* `amazon_brand_store_page_views`
* `amazon_brand_store_engagement_events`

For eligible advertisers and instances, the associated audience table can be used for AMC audience creation without a Paid feature subscription:

* `amazon_brand_store_page_views(_non_endemic)_for_audiences`
* `amazon_brand_store_engagement_events(_non_endemic)_for_audiences`

Refer to [Amazon brand store insights](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/brand_store_insights_paid).

## Amazon retail purchases (ARP)

**Availability:** AMC accounts/instances associated with US, CA, JP, AU, FR, IT, ES, UK, DE, MX, BR, NL, SE, PL, BE, AE, SA, TR, EG, IE, ZA, NG, SG, IN marketplaces

**Eligibility:** At least one Amazon Ads account associated with your AMC instance must be linked to a selling partner account (Vendor Central or Seller Central) that sells products in the Amazon Store. Instances whose Amazon Ads accounts are not linked to a selling partner account with products, such as instances with only Amazon DSP advertisers that have no linked selling partner account, are not eligible.

**Contains signals from:** US, CA, JP, AU, FR, IT, ES, UK, DE, MX, BR, NL, SE, PL, BE, AE, SA, TR, EG, IE, ZA, NG, SG, IN marketplaces for measurement. Audiences are available in all marketplaces, but data from the United Kingdom and European Union (EU) is excluded from the audiences table.

* For Vendor Central accounts, the scope of data will match what is shown in Vendor Central "Reports \> Retail Analytics \> Sales \> Distributor View \= Manufacturing".
* For Seller Central accounts, the data scope should match what appears in Seller Central "Reports \> Business Reports \> By ASIN Detail" report.

Amazon Retail Purchases is a paid feature dataset available in AMC that contains up to five years (60 months) of historical Amazon store purchase data.

* `amazon_retail_purchases`

For eligible advertisers and instances, the associated audience table can be used for AMC audience creation without a Paid feature subscription (excluding data from the United Kingdom and European Union):

* `amazon_retail_purchases_for_audiences`

Refer to [Amazon retail purchases](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/amazon_retail_purchase_paid).

## Amazon Prime Video Insights (PVI)

**Availability:** AMC accounts/instances associated with the US, CA, JP, AU, FR, IT, ES, UK, DE, MX, BR, NL, SE, PL, BE, AE, SA, TR, EG, IE, ZA, NG, SG, IN marketplaces

**Eligibility:** All AMC advertisers and instances within the eligible marketplaces above. Data coverage is limited to users an advertiser has reached through an upstream data join with ad traffic tables.

**Contains signals from:** US, CA, JP, AU, FR, IT, ES, UK, DE, MX, BR, NL, SE, PL, BE, AE, SA, TR, EG, IE, ZA, NG, SG, IN marketplaces

 Note Amazon Prime Video Insights (PVI) is a separate, distinct dataset from [Amazon Prime Video Channel Insights](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/prime_video_channel_insights_paid) (PVCI) below. PVI measures Prime Video streaming/viewership signals; PVCI measures Prime Video Channel subscription and streaming signals.Amazon Prime Video Insights helps advertisers better understand the entertainment preferences of their customers and how these intersect with other customer behaviors, enabling custom attribution for subscriptions, re\-engagement campaigns, and audience overlap analysis. The PVI lookback window is 13 months.

* `pv_streaming_events_feed`

For eligible advertisers and instances, the associated audience table can be used for AMC audience creation without a Paid feature subscription:

* `pv_streaming_events_feed_for_audiences`

Refer to [Amazon Prime Video Insights](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/prime-video-insights-paid) for full documentation.

## Amazon Prime Video Channel insights (PVCI)

**Availability:** AMC accounts/instances associated with the US/CA/JP/AU/FR/IT/ES/UK/DE marketplaces

**Eligibility:** Only Amazon advertisers that operate Prime Video Channels

**Contains signals from:** US/CA/JP/AU/FR/IT/ES/UK/DE marketplaces

Amazon Prime Video Channel Insights is a collection of two AMC data views that represent Prime Video Channel subscriptions and streaming signals. (See [Amazon Prime Video Insights](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/paid_features_overview#amazon-prime-video-insights-pvi) above for the separate PVI dataset.)

* `amazon_pvc_enrollments`
* `amazon_pvc_streaming_events_feed`

For eligible advertisers and instances, the associated audience table can be used for AMC audience creation without a Paid feature subscription:

* `amazon_pvc_enrollments_for_audiences`
* `amazon_pvc_streaming_events_feed_for_audiences`

Refer to [Amazon Prime Video Channel insights](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/prime_video_channel_insights_paid).

## NCS CPG Insights Stream

**Availability:** AMC accounts/instances associated with the US AMC account marketplace

**Eligibility:** Any advertiser

**Contains signals from:** US marketplace

The NCS CPG Insights Stream data source provides modeled offline transaction signals for all US households.

* `ncs_cpg_insights_stream`

For eligible advertisers and instances, the associated audience table can be used for AMC audience creation without a Paid feature subscription:

* `ncs_cpg_insights_stream_for_audiences`

 Note Although you can use the audience view without a subscription, a CPM fee of $2 is applied on activation of the audience in Amazon DSP. Note NCS audience tables are not supported for Lookalike audience creation, or for audience activation in sponsored ads.Refer to [NCS CPG Insights Stream](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/cpg_insights_stream_paid).

## Experian vehicle purchases insights

**Availability:** AMC accounts associated with the US marketplace

**Eligibility:** Any advertiser

**Contains signals from:** US marketplace

Experian Vehicle Purchase Insights allows you to measure the impact of their advertising on actual vehicle purchases, better understand path to purchase, and learn about how they can reach new audiences.

* `experian_vehicle_purchases`

There is no associated audience table.

Refer to [Experian Vehicle Purchase Insights](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/experian_paid).
