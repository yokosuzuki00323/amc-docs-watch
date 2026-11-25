# AMC consent management | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/amc_consent_management

# Consent management in AMC

Was this page helpful?If you transmit or make available to Amazon Ads any personal information in connection with your use of any Amazon advertising services in the UK and EEA, you must share a valid consent signal and the country code in which consent was granted by the customer.

## Consent Signals

You can use one of the following to communicate privacy choices of UK and EEA users to Amazon Ads:

* The IAB European Transparency \& Consent Framework (TCF) signal(s)
* Global Privacy Protocol (GPP)
* Amazon Consent Signal (ACS)

 Note Please do not send multiple signals. If multiple are provided, Amazon Ads will use TCF and ignore ACS.### Country Code

You must share a country code when passing consented data of customers to Amazon Ads. The country code is a 2\-character string in the ISO 3166 format that indicates in which country the consent was given (for example, US, GB or DE).

 Note Data uploaded without specifying a country code will be rejected. ### What is Amazon Consent Signal?

In addition to supporting the Interactive Advertising Bureau (IAB) Transparency \& Consent Framework (TCF) signal and Global Privacy Protocol (GPP), Amazon Ads has introduced Amazon Consent Signal (ACS) which enables you to transmit the privacy choices of end users to Amazon Ads in the UK and EEA. There are three required parameters:

`CountryCode`: The Country Code indicates where consent was given by the user.
Acceptable values: 2\-character ISO 3166 format (for example, US, GB, DE).

If `CountryCode` is missing, Amazon may reject the data record entirely.

`amzn_user_data`: Indicates whether the user has consented to Amazon processing personal data (for example, an advertising identifier) for advertising purposes.
Acceptable values are `GRANTED` or `DENIED`.

`amzn_ad_storage`: Indicates whether the user has given Amazon consent to read or write advertising cookies or similar technologies on the device of the user.
Accepted inputs: `GRANTED`, `DENIED`, or `NULL`.

 Note When `amzn_ad_storage` is not relevant the acceptable value is `NULL` or third\-parties can exclude the parameter entirely.  Important AMC and Ads data manager will accept TCF, GPP, and ACS consent signals. AMC and Ads data manager will respect provided consent, rejecting records if denied. Advertisers and third\-party providers are advised to update their integrations to include country codes and consent information to ensure uninterrupted services. Please refer to [Sending Personal Information to Amazon Ads \& Amazon Consent Signal requirements](https://advertising.amazon.com/resources/ad-policy/consent-signal-requirements?ref_=a20m_us_spcs_conre) to know more about the policy.

The above\-mentioned data decoration standards for country codes and consent signals apply to all advertisers and 3Ps using AMC.

* Provide consent for uploads using [Advertiser data upload APIs](/API/docs/en-us/guides/amazon-marketing-cloud/advertiser-data-upload/advertiser-data-sets)
* Provide consent for data in [AMC \- AWS Clean Rooms collaboration instances](/API/docs/en-us/guides/amazon-marketing-cloud/acr/5_data_prep)
