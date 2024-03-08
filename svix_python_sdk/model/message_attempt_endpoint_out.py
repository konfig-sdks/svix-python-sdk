# coding: utf-8

"""
    Svix API

    Welcome to the Svix API documentation!  Useful links: [Homepage](https://www.svix.com) | [Support email](mailto:support+docs@svix.com) | [Blog](https://www.svix.com/blog/) | [Slack Community](https://www.svix.com/slack/)  # Introduction  This is the reference documentation and schemas for the [Svix webhook service](https://www.svix.com) API. For tutorials and other documentation please refer to [the documentation](https://docs.svix.com).  ## Main concepts  In Svix you have four important entities you will be interacting with:  - `messages`: these are the webhooks being sent. They can have contents and a few other properties. - `application`: this is where `messages` are sent to. Usually you want to create one application for each user on your platform. - `endpoint`: endpoints are the URLs messages will be sent to. Each application can have multiple `endpoints` and each message sent to that application will be sent to all of them (unless they are not subscribed to the sent event type). - `event-type`: event types are identifiers denoting the type of the message being sent. Event types are primarily used to decide which events are sent to which endpoint.   ## Authentication  Get your authentication token (`AUTH_TOKEN`) from the [Svix dashboard](https://dashboard.svix.com) and use it as part of the `Authorization` header as such: `Authorization: Bearer ${AUTH_TOKEN}`. For more information on authentication, please refer to the [authentication token docs](https://docs.svix.com/api-keys).     ## Code samples  The code samples assume you already have the respective libraries installed and you know how to use them. For the latest information on how to do that, please refer to [the documentation](https://docs.svix.com/).   ## Idempotency  Svix supports [idempotency](https://en.wikipedia.org/wiki/Idempotence) for safely retrying requests without accidentally performing the same operation twice. This is useful when an API call is disrupted in transit and you do not receive a response.  To perform an idempotent request, pass the idempotency key in the `Idempotency-Key` header to the request. The idempotency key should be a unique value generated by the client. You can create the key in however way you like, though we suggest using UUID v4, or any other string with enough entropy to avoid collisions.  Svix's idempotency works by saving the resulting status code and body of the first request made for any given idempotency key for any successful request. Subsequent requests with the same key return the same result for a period of up to 12 hours.  Please note that idempotency is only supported for `POST` requests.   ## Cross-Origin Resource Sharing  This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/). And that allows cross-domain communication from the browser. All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site. 

    The version of the OpenAPI document: 1.20.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from svix_python_sdk import schemas  # noqa: F401


class MessageAttemptEndpointOut(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "responseStatusCode",
            "endpointId",
            "response",
            "msgId",
            "id",
            "triggerType",
            "url",
            "status",
            "timestamp",
        }
        
        class properties:
            
            
            class url(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'uri'
                    max_length = 65536
                    min_length = 1
            response = schemas.StrSchema
            responseStatusCode = schemas.IntSchema
        
            @staticmethod
            def status() -> typing.Type['MessageStatus']:
                return MessageStatus
        
            @staticmethod
            def triggerType() -> typing.Type['MessageAttemptTriggerType']:
                return MessageAttemptTriggerType
            msgId = schemas.StrSchema
            endpointId = schemas.StrSchema
            id = schemas.StrSchema
            timestamp = schemas.DateTimeSchema
        
            @staticmethod
            def msg() -> typing.Type['MessageOut']:
                return MessageOut
            __annotations__ = {
                "url": url,
                "response": response,
                "responseStatusCode": responseStatusCode,
                "status": status,
                "triggerType": triggerType,
                "msgId": msgId,
                "endpointId": endpointId,
                "id": id,
                "timestamp": timestamp,
                "msg": msg,
            }
    
    responseStatusCode: MetaOapg.properties.responseStatusCode
    endpointId: MetaOapg.properties.endpointId
    response: MetaOapg.properties.response
    msgId: MetaOapg.properties.msgId
    id: MetaOapg.properties.id
    triggerType: 'MessageAttemptTriggerType'
    url: MetaOapg.properties.url
    status: 'MessageStatus'
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["response"]) -> MetaOapg.properties.response: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["responseStatusCode"]) -> MetaOapg.properties.responseStatusCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'MessageStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["triggerType"]) -> 'MessageAttemptTriggerType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["msgId"]) -> MetaOapg.properties.msgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endpointId"]) -> MetaOapg.properties.endpointId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["msg"]) -> 'MessageOut': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["url", "response", "responseStatusCode", "status", "triggerType", "msgId", "endpointId", "id", "timestamp", "msg", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["response"]) -> MetaOapg.properties.response: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["responseStatusCode"]) -> MetaOapg.properties.responseStatusCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'MessageStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["triggerType"]) -> 'MessageAttemptTriggerType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["msgId"]) -> MetaOapg.properties.msgId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endpointId"]) -> MetaOapg.properties.endpointId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["msg"]) -> typing.Union['MessageOut', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["url", "response", "responseStatusCode", "status", "triggerType", "msgId", "endpointId", "id", "timestamp", "msg", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        responseStatusCode: typing.Union[MetaOapg.properties.responseStatusCode, decimal.Decimal, int, ],
        endpointId: typing.Union[MetaOapg.properties.endpointId, str, ],
        response: typing.Union[MetaOapg.properties.response, str, ],
        msgId: typing.Union[MetaOapg.properties.msgId, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        triggerType: 'MessageAttemptTriggerType',
        url: typing.Union[MetaOapg.properties.url, str, ],
        status: 'MessageStatus',
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, ],
        msg: typing.Union['MessageOut', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MessageAttemptEndpointOut':
        return super().__new__(
            cls,
            *args,
            responseStatusCode=responseStatusCode,
            endpointId=endpointId,
            response=response,
            msgId=msgId,
            id=id,
            triggerType=triggerType,
            url=url,
            status=status,
            timestamp=timestamp,
            msg=msg,
            _configuration=_configuration,
            **kwargs,
        )

from svix_python_sdk.model.message_attempt_trigger_type import MessageAttemptTriggerType
from svix_python_sdk.model.message_out import MessageOut
from svix_python_sdk.model.message_status import MessageStatus
