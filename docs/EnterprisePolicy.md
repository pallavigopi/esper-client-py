# EnterprisePolicy
> esperclient.models.enterprise_policy

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique Policy identifier | [optional] 
**enterprise** | **str** | Url of the enterprise resource | 
**url** | **str** | URL link to policy | [optional] 
**name** | **str** | Name of the Policy | 
**description** | **str** | Details regarding the Policy | [optional] 
**device_count** | **int** | Count of Devices with this policy applied | [optional] 
**google_policy_id** | **str** | Id of the Google policy | [optional] 
**policy** | [**EnterprisePolicyData**](EnterprisePolicyData.md) |  | 
**updated_on** | **datetime** | Last-Updated Timestamp of Policy | [optional] 
**created_on** | **datetime** | Creation Timestamp of Policy | [optional] 
**is_active** | **bool** | Is this policy currently active | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


