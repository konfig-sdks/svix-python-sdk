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


class EndpointMessageOut(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A model containing information on a given message plus additional fields on the last attempt for that message.
    """


    class MetaOapg:
        required = {
            "payload",
            "eventType",
            "id",
            "status",
            "timestamp",
        }
        
        class properties:
        
            @staticmethod
            def status() -> typing.Type['MessageStatus']:
                return MessageStatus
            
            
            class eventType(
                schemas.StrSchema
            ):
                pass
            payload = schemas.DictSchema
            id = schemas.StrSchema
            timestamp = schemas.DateTimeSchema
        
            @staticmethod
            def tags() -> typing.Type['EndpointMessageOutTags']:
                return EndpointMessageOutTags
            
            
            class nextAttempt(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nextAttempt':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class eventId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
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
            def channels() -> typing.Type['EndpointMessageOutChannels']:
                return EndpointMessageOutChannels
            __annotations__ = {
                "status": status,
                "eventType": eventType,
                "payload": payload,
                "id": id,
                "timestamp": timestamp,
                "tags": tags,
                "nextAttempt": nextAttempt,
                "eventId": eventId,
                "channels": channels,
            }
    
    payload: MetaOapg.properties.payload
    eventType: MetaOapg.properties.eventType
    id: MetaOapg.properties.id
    status: 'MessageStatus'
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'MessageStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eventType"]) -> MetaOapg.properties.eventType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payload"]) -> MetaOapg.properties.payload: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> 'EndpointMessageOutTags': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextAttempt"]) -> MetaOapg.properties.nextAttempt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eventId"]) -> MetaOapg.properties.eventId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channels"]) -> 'EndpointMessageOutChannels': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "eventType", "payload", "id", "timestamp", "tags", "nextAttempt", "eventId", "channels", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'MessageStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eventType"]) -> MetaOapg.properties.eventType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payload"]) -> MetaOapg.properties.payload: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union['EndpointMessageOutTags', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextAttempt"]) -> typing.Union[MetaOapg.properties.nextAttempt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eventId"]) -> typing.Union[MetaOapg.properties.eventId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channels"]) -> typing.Union['EndpointMessageOutChannels', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "eventType", "payload", "id", "timestamp", "tags", "nextAttempt", "eventId", "channels", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        payload: typing.Union[MetaOapg.properties.payload, dict, frozendict.frozendict, ],
        eventType: typing.Union[MetaOapg.properties.eventType, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        status: 'MessageStatus',
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, ],
        tags: typing.Union['EndpointMessageOutTags', schemas.Unset] = schemas.unset,
        nextAttempt: typing.Union[MetaOapg.properties.nextAttempt, None, str, datetime, schemas.Unset] = schemas.unset,
        eventId: typing.Union[MetaOapg.properties.eventId, None, str, schemas.Unset] = schemas.unset,
        channels: typing.Union['EndpointMessageOutChannels', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EndpointMessageOut':
        return super().__new__(
            cls,
            *args,
            payload=payload,
            eventType=eventType,
            id=id,
            status=status,
            timestamp=timestamp,
            tags=tags,
            nextAttempt=nextAttempt,
            eventId=eventId,
            channels=channels,
            _configuration=_configuration,
            **kwargs,
        )

from svix_python_sdk.model.endpoint_message_out_channels import EndpointMessageOutChannels
from svix_python_sdk.model.endpoint_message_out_tags import EndpointMessageOutTags
from svix_python_sdk.model.message_status import MessageStatus