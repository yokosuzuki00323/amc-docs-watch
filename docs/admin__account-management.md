# Amazon Marketing Cloud - Account Management | Amazon Ads API
**URL:** https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/admin/account-management

# AMC account management

Was this page helpful?An AMC account represents an advertiser or partner organization. Each account can have one or more "instances" associated with the account. This top\-level account, also known as an AMC entity, is managed by an account administrator, who can then invite other users to access or administer the account.

 Note In addition to AMC accounts, **manager accounts** can be used with AMC. A manager account can own multiple AMC instances, each containing multiple advertisers linked to the manager account, without an AMC account provisioned by an AdTech AE. For an overview of manager accounts and how to create one, see [Manager accounts in the Amazon Ads API](/API/docs/en-us/guides/account-management/authorization/manager-accounts); to create and manage manager accounts programmatically, see the [Manager Account API developer guide](/API/docs/en-us/guides/account-management/manager-account-api). For how advertiser access and scope work for manager account instances, see [Instance management](/API/docs/en-us/guides/amazon-marketing-cloud/admin/instance-management#manager-account-instances).We will refer to the account administrator as "admin" or "admin user" in this section. The admin user has permissions to associate and manage one or more AMC instances, and add users to instances in the account.

In the sections below, we will discuss how to manage an account using the AMC account administration APIs and perform tasks to manage users in the organization.

## Retrieve AMC account Id

To work with your AMC account, you must know your `AMC account Id`.

When you register for Amazon Ads, and are approved for AMC access, an Amazon Ads account executive would have created your AMC account and provided you your AMC account Id. The AMC account ID, also known as the entity identifier, is a unique alphanumeric code that identifies your AMC account.

### Retrieve AMC account Id from AMC console

If you already have access to the AMC console, you can log in using your credentials and find your AMC account ID in the URL. The AMC account ID is the alphanumeric code prefixed with "ENTITY". For example, a valid AMC account ID (entity identifier) could be "ENTITY1AA1AA11AAA1".

### Retrieve AMC account Id using AMC APIs

Alternatively, if you have already onboarded Amazon Ads API using your Login with Amazon credentials, use the `GET` operation of the `/amc/accounts` resource.

The mandatory header parameters for this operation are:

| Header | Description |
| --- | --- |
| `Amazon-Advertising-API-ClientId` | The client ID related to a Login with Amazon application. |
| `Authorization` | Login with Amazon token in the form of Bearer `{token}`. |

#### Sample request

```

curl --location 'https://advertising-api.amazon.com/amc/accounts'
--header 'Authorization: Bearer xxxxxxxxxxxx`
--header 'Amazon-Advertising-API-ClientID: amzn1.application-oa2-client.xxxxxxxxxx'
```
#### Sample response

```
{
"amcAccounts":
[
    {
        "accountId": "ENTITY1xxxxxxxxxxxx ",
        "accountName": "AMC Demo Account",
        "marketplaceId": "ATVPDKIKX0DER"
    }
    ]
}
```
Note the value of the `accountId` in the above response and use that to pass it as the value for the `Amazon-Advertising-API-AdvertiserId` header parameter, required for most AMC calls.

### Retrieve advertiser accounts

For AMC to access data from your Amazon advertising campaigns, you will need to provide your advertiser account information. Visit the pages below to know how to retrieve your advertiser account ids.
[Retrieve Amazon DSP account id.](/API/docs/en-us/guides/get-started/retrieve-profiles)
[Retrieve sponsored ads account id (known as entity id.)](/API/docs/en-us/guides/account-management/accounts/retrieve-accounts)

## Manage users

As an AMC administrator, you are your organization's nominated "system admin". You can manage multiple advertising accounts from your organization and can programmatically invite users from your organization to join the AMC account.

### Invite users

Users can be invited to join your organization's AMC account as administrators or as viewers.
Use the `POST /user-invitations` endpoint to create an invitation.

 Note The value for the `Amazon-Ads-AccountId` header parameter is the AMC account identifier.To create an admin user, the `permissionSet` property in your request payload must be set to `admin`. For a non\-admin user, the `permissionSet` property must be set to `viewer`.

```
{
    "userInvitationRequests": [
        {
            "user":{
                "emailAddress":"advertiser@example.com",
                "userName": "Advertiser"
            },
            "permissionSet":{
                "type":"ROLE",
                "role": {
                    "name":"viewer"
                }
            }
        }
    ],
    "notifyInvitedUsers":true
}
```
Invited users are sent an email with the `invitationId`. To join the AMC account, the invited user must accept the AMC terms and conditions to [redeem the invite](/API/docs/en-us/guides/amazon-marketing-cloud/admin/account-management#redeem-invite).

### Redeem invite

 Note This step must be completed by the user who has been invited to join the AMC instance.The invited user must click the link in the invitation email to view and accept the terms.

### Update user invitation

To update user invitations that you have already sent, use the `PUT /user-invitations` endpoint. You can update the invitation `state` to revoke the invitation or resend the invitation.

For more details on the user invitation management APIs, see [the user invitation reference documentation](/API/docs/en-us/user-invitations).
