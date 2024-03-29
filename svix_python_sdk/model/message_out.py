# coding: utf-8

"""
    Svix API

    Welcome to the Svix API documentation!  Useful links: [Homepage](https://www.svix.com) | [Support email](mailto:support+docs@svix.com) | [Blog](https://www.svix.com/blog/) | [Slack Community](https://www.svix.com/slack/)  # Introduction  This is the reference documentation and schemas for the [Svix webhook service](https://www.svix.com) API. For tutorials and other documentation please refer to [the documentation](https://docs.svix.com).  ## Main concepts  In Svix you have four important entities you will be interacting with:  - `messages`: these are the webhooks being sent. They can have contents and a few other properties. - `application`: this is where `messages` are sent to. Usually you want to create one application for each user on your platform. - `endpoint`: endpoints are the URLs messages will be sent to. Each application can have multiple `endpoints` and each message sent to that application will be sent to all of them (unless they are not subscribed to the sent event type). - `event-type`: event types are identifiers denoting the type of the message being sent. Event types are primarily used to decide which events are sent to which endpoint.   ## Authentication  Get your authentication token (`AUTH_TOKEN`) from the [Svix dashboard](https://dashboard.svix.com) and use it as part of the `Authorization` header as such: `Authorization: Bearer ${AUTH_TOKEN}`. For more information on authentication, please refer to the [authentication token docs](https://docs.svix.com/api-keys).     ## Code samples  The code samples assume you already have the respective libraries installed and you know how to use them. For the latest information on how to do that, please refer to [the documentation](https://docs.svix.com/).   ## Idempotency  Svix supports [idempotency](https://en.wikipedia.org/wiki/Idempotence) for safely retrying requests without accidentally performing the same operation twice. This is useful when an API call is disrupted in transit and you do not receive a response.  To perform an idempotent request, pass the idempotency key in the `Idempotency-Key` header to the request. The idempotency key should be a unique value generated by the client. You can create the key in however way you like, though we suggest using UUID v4, or any other string with enough entropy to avoid collisions.  Svix's idempotency works by saving the resulting status code and body of the first request made for any given idempotency key for any successful request. Subsequent requests with the same key return the same result for a period of up to 12 hours.  Please note that idempotency is only supported for `POST` requests.   ## Cross-Origin Resource Sharing  This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/). And that allows cross-domain communication from the browser. All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site. 

    The version of the OpenAPI document: 1.21.0
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


class MessageOut(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "payload",
            "eventType",
            "id",
            "timestamp",
        }
        
        class properties:
            
            
            class eventType(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 256
                    regex=[{
                        'pattern': r'^[a-zA-Z0-9\-_.]+$',
                    }]
            payload = schemas.DictSchema
            id = schemas.StrSchema
            timestamp = schemas.DateTimeSchema
        
            @staticmethod
            def tags() -> typing.Type['MessageOutTags']:
                return MessageOutTags
            
            
            class eventId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 256
                    min_length = 1
                    regex=[{
                        'pattern': r'^[a-zA-Z0-9\-_.]+$',
                    }]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'eventId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def channels() -> typing.Type['MessageOutChannels']:
                return MessageOutChannels
            __annotations__ = {
                "eventType": eventType,
                "payload": payload,
                "id": id,
                "timestamp": timestamp,
                "tags": tags,
                "eventId": eventId,
                "channels": channels,
            }
    
    payload: MetaOapg.properties.payload
    eventType: MetaOapg.properties.eventType
    id: MetaOapg.properties.id
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eventType"]) -> MetaOapg.properties.eventType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payload"]) -> MetaOapg.properties.payload: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> 'MessageOutTags': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eventId"]) -> MetaOapg.properties.eventId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channels"]) -> 'MessageOutChannels': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["eventType", "payload", "id", "timestamp", "tags", "eventId", "channels", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eventType"]) -> MetaOapg.properties.eventType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payload"]) -> MetaOapg.properties.payload: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union['MessageOutTags', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eventId"]) -> typing.Union[MetaOapg.properties.eventId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channels"]) -> typing.Union['MessageOutChannels', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["eventType", "payload", "id", "timestamp", "tags", "eventId", "channels", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        payload: typing.Union[MetaOapg.properties.payload, dict, frozendict.frozendict, ],
        eventType: typing.Union[MetaOapg.properties.eventType, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, ],
        tags: typing.Union['MessageOutTags', schemas.Unset] = schemas.unset,
        eventId: typing.Union[MetaOapg.properties.eventId, None, str, schemas.Unset] = schemas.unset,
        channels: typing.Union['MessageOutChannels', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MessageOut':
        return super().__new__(
            cls,
            *args,
            payload=payload,
            eventType=eventType,
            id=id,
            timestamp=timestamp,
            tags=tags,
            eventId=eventId,
            channels=channels,
            _configuration=_configuration,
            **kwargs,
        )

from svix_python_sdk.model.message_out_channels import MessageOutChannels
from svix_python_sdk.model.message_out_tags import MessageOutTags
