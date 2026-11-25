# Amazon retail purchase | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/datasources/amazon_retail_purchase_paid

# Amazon Retail Purchases in AMC

Was this page helpful?**Analytics table:**

* `amazon_retail_purchases`

**Audiences table:**

* `amazon_retail_purchases_for_audiences`

The Amazon Retail Purchases (ARP) dataset (`amazon_retail_purchases`) enables advertisers to analyze long\-term (up to 60 months) customer purchase behavior and create more comprehensive insights.

 Note Starting June 1, 2026, you can query this dataset at no cost through December 31, 2026 in every region where it is available. If you already have an active subscription, it will automatically convert to zero dollars. For more details, refer to [Amazon 1P signals available at no cost](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/paid_features_overview#amazon-1p-signals-available-at-no-cost).### Availability

This data source is available for measurement queries through a Paid features subscription in the US, CA, JP, AU, FR, IT, ES, UK, DE, MX, BR, NL, SE, PL, BE, AE, SA, TR, EG, IE, ZA, NG, SG, IN marketplaces.

Data from the United Kingdom and European Union (EU) regions will be excluded from audience creation.

### Subscription and access requirements

* This dataset is available through subscription. You can opt into a 60\-day free trial, after which a subscription is necessary to access the dataset.
* Check the Sponsored Ads accounts configured to your AMC instance configuration to ensure the correct Vendor/Seller Central accounts are associated. You can verify the associations in **Ads Console \> Administration (gear icon) \> Account access \& settings \> Selling account**.

	+ For **Vendor Central** accounts, the scope of data in ARP will match with what is shown in the Vendor Central under **Reports \> Retail Analytics \> Sales \> Distributor View \= Manufacturing**.
	+ For **Seller Central** accounts, the scope of data in ARP should match with what is shown in the Seller Central **Reports \> Business Reports \> By ASIN Detail** report.

 Important The ARP dataset in AMC contains up to 60 months (5 years) of historical purchase data, while other datasets retain between 13 months and 5 years of records, depending on the data view. For the retention window of each data view, refer to [AMC data retention](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/data-retention). Exercise caution when joining the retail purchase data with other AMC datasets, as failing to account for the mismatched time windows could lead to inaccurate analysis and incorrect conclusions. Note The promotional signal columns described in [Working with Promotional Signals](/API/docs/en-us/guides/amazon-marketing-cloud/datasources/amazon_retail_purchase_paid#working-with-promotional-signals) below have a shorter history than the rest of the ARP dataset: 2 years (starting September 24, 2024\), not the full 5\-year (60\-month) window. Account for this narrower history separately when joining or trending the promotional fields.### Conversion datasets

While the AMC `conversions` and `conversions_all` (referred to as CONV) datasets may appear similar, they are different in the following ways:

| Aspect | CONV | ARP |
| --- | --- | --- |
| Scope of conversion types | Various conversion event types (purchases, considerations, pixel\-based conversions). | Amazon store purchase conversion events only. |
| Scope of events | Advertising\-centric (can include promoted, brand\-halo, and brand\-owned `ASIN` items). | Entire purchase activity in Amazon store, regardless of advertising. |
| Data pipelines and restatements | Sourced from advertising data pipelines; subject to restatements and advertising augmentation. | Sourced from retail data pipeline including restatements, and more closely matched data found in other Amazon reporting surfaces like Vendor Central. |

The AMC dataset associated with ARP is `amazon_retail_purchases`.

## amazon\_retail\_purchases

| Field name | Data type | Description | Aggregation Threshold |
| --- | --- | --- | --- |
| `asin` | `STRING` | `ASIN` is the abbreviation for Amazon Standard Identification Number. This represents the item associated with the retail event. A unique block of letters and/or numbers that identify all products sold on Amazon. | `LOW` |
| `asin_brand` | `STRING` | `ASIN` item merchant brand name. | `LOW` |
| `asin_name` | `STRING` | `ASIN` item name. | `LOW` |
| `asin_parent` | `STRING` | The Amazon Standard Identification Number (`ASIN`) that is the parent of this `ASIN` for the retail event. | `LOW` |
| `coupon_discount_amt` | `DECIMAL` | The discount applied to the order line item from a clipped coupon, in the currency of the marketplace where the purchase occurred. | `NONE` |
| `coupon_discount_id` | `STRING` | The unique identifier of the coupon discount applied to the product at the time of purchase. A coupon is a discount that shoppers clip before checkout. | `LOW` |
| `coupon_discount_name` | `STRING` | The title of the coupon discount applied to the product at the time of purchase. | `LOW` |
| `coupon_discount_type` | `STRING` | The category of the coupon discount applied to the product at the time of purchase. Values may include `AMOUNT_OFF`, `PERCENT_OFF`. | `LOW` |
| `currency_code` | `STRING` | ISO currency code of the retail event. | `LOW` |
| `event_id` | `STRING` | Unique identifier of the retail event record. In the data set, each row has a unique `event_id`. This `event_id` can have a many\-to\-one relationship with `purchase_id`. | `VERY_HIGH` |
| `is_business_flag` | `BOOLEAN` | Indicates whether the retail event is associated with "Amazon Business" program. | `LOW` |
| `is_gift_flag` | `BOOLEAN` | Indicates whether the retail event is associated with "send an order as a gift". | `LOW` |
| `marketplace_id` | `INTEGER` | Marketplace ID of where the retail event occurred. | `INTERNAL` |
| `marketplace_name` | `STRING` | Name of the marketplace where the retail event occurred. Example values include `AMAZON.COM`, `AMAZON.CO.UK`, etc. | `LOW` |
| `net_unit_price` | `DECIMAL` | The net per\-unit price for the product after Lightning Deals (price discount), point\-of\-sale, and coupon discounts are applied to the transaction. All other price discounts are reflected in the unit price. | `NONE` |
| `no_3p_trackers` | `BOOLEAN` | Is this item not allowed to use 3P tracking. | `NONE` |
| `origin_session_id` | `STRING` | Describes the session when the retail item was added to cart. | `VERY_HIGH` |
| `point_of_sale_discount_amt` | `DECIMAL` | The discount applied to the order line item by a cart\-based point\-of\-sale promotion, in the currency of the marketplace where the purchase occurred. | `NONE` |
| `point_of_sale_discount_id` | `STRING` | The unique identifier of the point\-of\-sale discount applied to the product at the time of purchase. A point\-of\-sale discount is applied at checkout when eligibility conditions are met and does not change the product's displayed price. | `LOW` |
| `point_of_sale_discount_name` | `STRING` | The title of the point\-of\-sale discount applied to the product at the time of purchase. | `LOW` |
| `point_of_sale_discount_type` | `STRING` | The category of the point\-of\-sale discount applied to the product at the time of purchase. Values may include `BUY_X_GET_AMOUNT_OFF`, `BUY_X_GET_PERCENT_OFF`. | `LOW` |
| `price_discount_amt` | `DECIMAL` | The reduction in the product's price from a price discount, measured as the difference between the product's average selling price during the 90 days preceding the promotion start date and the product's discounted price, in the currency of the marketplace where the purchase occurred. | `NONE` |
| `price_discount_id` | `STRING` | The unique identifier of the price discount applied to the product at the time of purchase. A price discount reduces the product's displayed price before it is added to the cart. | `LOW` |
| `price_discount_name` | `STRING` | The title of the price discount applied to the product at the time of purchase. | `LOW` |
| `price_discount_type` | `STRING` | The category of the price discount applied to the product at the time of purchase. Values may include `BEST_DEAL`, `DEAL_OF_THE_DAY`, `LIGHTNING_DEAL`. | `LOW` |
| `purchase_date_utc` | `DATE` | Date of the retail event in UTC. | `LOW` |
| `purchase_day_utc` | `INTEGER` | Day of the month of the retail event in UTC. | `LOW` |
| `purchase_dt_hour_utc` | `TIMESTAMP` | Timestamp of the retail event in UTC truncated to the hour. | `LOW` |
| `purchase_dt_utc` | `TIMESTAMP` | Timestamp of the retail event in UTC. | `MEDIUM` |
| `purchase_hour_utc` | `INTEGER` | Hour of the day of the retail event in UTC. | `LOW` |
| `purchase_id` | `STRING` | Unique identifier of the retail purchase record. This `purchase_id` can have a one\-to\-many relationship with `event_id`. | `VERY_HIGH` |
| `purchase_month_utc` | `INTEGER` | Month of the conversion event in UTC. | `LOW` |
| `purchase_order_method` | `STRING` | Enumerated descriptor of how the shopper purchased the item. S \= Shopping Cart. B \= Buy Now. 1 \= 1\-Click Buy. | `LOW` |
| `purchase_program_name` | `STRING` | Indicates the purchase program associated with the retail event. | `LOW` |
| `purchase_session_id` | `STRING` | Describes the session when the retail item was purchased. | `VERY_HIGH` |
| `purchase_units_sold` | `LONG` | Total quantity of retail items associated with the retail event. A record can have multiple units sold of a single retail item. | `NONE` |
| `unit_price` | `DECIMAL` | Per unit price of the product sold. Includes price discounts except when `price_discount_type` \= LIGHTNING\_DEAL. | `NONE` |
| `user_id` | `STRING` | User ID associated with the retail event (the user ID of the shopper that purchased the item). | `VERY_HIGH` |
| `user_id_type` | `STRING` | Type of user ID. The only value for this data set is `adUserId`. | `LOW` |

## Working with Promotional Signals

The `amazon_retail_purchases` dataset includes promotional fields that show how shoppers responded to deals, discounts, and coupons at the purchase level. A few notes will help you interpret this data correctly.

* **What is included:** Promotional signals reflect only vendor or seller self\-funded promotions.
* **What is not included:** Subscribe \& Save discounts, Amazon\-funded promotions, and non\-monetary benefits such as loyalty or reward points are not included.
* **How discounts are grouped:** Promotions fall into three independent groups. Price discounts, such as Best Deals, change the displayed buy\-box price directly. Point\-of\-sale discounts, such as Buy X Get Y, apply at checkout when a condition is met. Coupons are a discount the shopper clips before checkout. Because the groups are independent, a single transaction can show a price discount, a point\-of\-sale discount, and a coupon at the same time.
* **Highest\-impacting promotion per type, per transaction:** For each transaction, the dataset reports only the single highest\-impacting promotion of each type — the one that provided the largest discount on the final price. If a purchase qualifies for more than one promotion of the same type, only the one with the greatest price impact is reported.
* **Net unit price:** `net_unit_price` is the per\-unit price after the highest\-impacting promotion of each type is applied. Point\-of\-sale discount and coupon amounts are always subtracted. The price discount is already reflected in the product's displayed price and is not subtracted again, except for Lightning Deals (`price_discount_type` \= LIGHTNING\_DEAL), which are excluded from the displayed price and are therefore subtracted.
* **Understanding the price discount amount:** `price_discount_amt` is the difference between the product's average selling price over the 90 days preceding the promotion and the discounted price. Price discounts are already reflected in the product's displayed price and are not subtracted again when `net_unit_price` is calculated, except for Lightning Deals (`price_discount_type` \= LIGHTNING\_DEAL), which are excluded from the displayed price and are therefore subtracted. Use it to gauge how far a price dropped relative to its recent typical price, rather than as a discount applied at checkout.
* **Reading blank values:** A blank promotional field means no qualifying vendor or seller self\-funded promotion was identified for that purchase — it does not mean the discount was zero. A discount amount can still be present on rows where the promotion ID or name is blank.
* **Data history:** 2 years of promotional history (starting September 24, 2024\) is available today. Design analyses around this window, and account for it separately when joining the promotional fields to datasets that carry a longer history.
* **Lightning Deals:** Lightning Deals are excluded from `unit_price`, unlike other price discounts, but are included in `net_unit_price`.
* **Calculating net unit price from unit price:** `net_unit_price` \= `unit_price`
	+ `coupon_discount_amt`
		- `point_of_sale_discount_amt`, minus `price_discount_amt` as well, but only when `price_discount_type` \= `LIGHTNING_DEAL`.
* **Calculating reference price:** Sum `net_unit_price`, `price_discount_amt`, `coupon_discount_amt`, and `point_of_sale_discount_amt`. Alternatively, calculate it from `unit_price`: reference price \= `unit_price`
	+ `price_discount_amt` (when `price_discount_type` !\= `LIGHTNING_DEAL`).
