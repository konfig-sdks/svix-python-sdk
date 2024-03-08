# coding: utf-8

"""
    Svix API

    Welcome to the Svix API documentation!  Useful links: [Homepage](https://www.svix.com) | [Support email](mailto:support+docs@svix.com) | [Blog](https://www.svix.com/blog/) | [Slack Community](https://www.svix.com/slack/)  # Introduction  This is the reference documentation and schemas for the [Svix webhook service](https://www.svix.com) API. For tutorials and other documentation please refer to [the documentation](https://docs.svix.com).  ## Main concepts  In Svix you have four important entities you will be interacting with:  - `messages`: these are the webhooks being sent. They can have contents and a few other properties. - `application`: this is where `messages` are sent to. Usually you want to create one application for each user on your platform. - `endpoint`: endpoints are the URLs messages will be sent to. Each application can have multiple `endpoints` and each message sent to that application will be sent to all of them (unless they are not subscribed to the sent event type). - `event-type`: event types are identifiers denoting the type of the message being sent. Event types are primarily used to decide which events are sent to which endpoint.   ## Authentication  Get your authentication token (`AUTH_TOKEN`) from the [Svix dashboard](https://dashboard.svix.com) and use it as part of the `Authorization` header as such: `Authorization: Bearer ${AUTH_TOKEN}`. For more information on authentication, please refer to the [authentication token docs](https://docs.svix.com/api-keys).     ## Code samples  The code samples assume you already have the respective libraries installed and you know how to use them. For the latest information on how to do that, please refer to [the documentation](https://docs.svix.com/).   ## Idempotency  Svix supports [idempotency](https://en.wikipedia.org/wiki/Idempotence) for safely retrying requests without accidentally performing the same operation twice. This is useful when an API call is disrupted in transit and you do not receive a response.  To perform an idempotent request, pass the idempotency key in the `Idempotency-Key` header to the request. The idempotency key should be a unique value generated by the client. You can create the key in however way you like, though we suggest using UUID v4, or any other string with enough entropy to avoid collisions.  Svix's idempotency works by saving the resulting status code and body of the first request made for any given idempotency key for any successful request. Subsequent requests with the same key return the same result for a period of up to 12 hours.  Please note that idempotency is only supported for `POST` requests.   ## Cross-Origin Resource Sharing  This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/). And that allows cross-domain communication from the browser. All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site. 

    The version of the OpenAPI document: 1.20.0
    Generated by: https://konfigthis.com
"""

from svix_python_sdk.paths.api_v1_app_app_id_endpoint.post import CreateNewRaw
from svix_python_sdk.paths.api_v1_app_app_id_endpoint_endpoint_id.get import GetEndpointRaw
from svix_python_sdk.paths.api_v1_app_app_id_endpoint_endpoint_id_headers.get import GetHeadersRaw
from svix_python_sdk.paths.api_v1_app_app_id_endpoint_endpoint_id_secret.get import GetSecretRaw
from svix_python_sdk.paths.api_v1_app_app_id_endpoint_endpoint_id_stats.get import GetStatsRaw
from svix_python_sdk.paths.api_v1_app_app_id_endpoint_endpoint_id_transformation.get import GetTransformationCodeRaw
from svix_python_sdk.paths.api_v1_app_app_id_endpoint.get import ListEndpointsRaw
from svix_python_sdk.paths.api_v1_app_app_id_endpoint_endpoint_id_headers.patch import PartiallySetHeadersRaw
from svix_python_sdk.paths.api_v1_app_app_id_endpoint_endpoint_id.patch import PartiallyUpdateRaw
from svix_python_sdk.paths.api_v1_app_app_id_endpoint_endpoint_id.delete import RemoveRaw
from svix_python_sdk.paths.api_v1_app_app_id_endpoint_endpoint_id_replay_missing.post import ReplayMissingWebhooksRaw
from svix_python_sdk.paths.api_v1_app_app_id_endpoint_endpoint_id_recover.post import ResendFailedWebhooksRaw
from svix_python_sdk.paths.api_v1_app_app_id_endpoint_endpoint_id_secret_rotate.post import RotateSecretRaw
from svix_python_sdk.paths.api_v1_app_app_id_endpoint_endpoint_id_send_example.post import SendExampleMessageRaw
from svix_python_sdk.paths.api_v1_app_app_id_endpoint_endpoint_id_transformation.patch import SetTransformationCodeRaw
from svix_python_sdk.paths.api_v1_app_app_id_endpoint_endpoint_id.put import UpdateEndpointRaw
from svix_python_sdk.paths.api_v1_app_app_id_endpoint_endpoint_id_headers.put import UpdateHeadersRaw


class EndpointApiRaw(
    CreateNewRaw,
    GetEndpointRaw,
    GetHeadersRaw,
    GetSecretRaw,
    GetStatsRaw,
    GetTransformationCodeRaw,
    ListEndpointsRaw,
    PartiallySetHeadersRaw,
    PartiallyUpdateRaw,
    RemoveRaw,
    ReplayMissingWebhooksRaw,
    ResendFailedWebhooksRaw,
    RotateSecretRaw,
    SendExampleMessageRaw,
    SetTransformationCodeRaw,
    UpdateEndpointRaw,
    UpdateHeadersRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
