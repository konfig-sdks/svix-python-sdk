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


class EndpointPatch(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            
            
            class version(
                schemas.IntSchema
            ):
                pass
            
            
            class rateLimit(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'uint16'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'rateLimit':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class uid(
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
                ) -> 'uid':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            url = schemas.StrSchema
            disabled = schemas.BoolSchema
        
            @staticmethod
            def filterTypes() -> typing.Type['EndpointPatchFilterTypes']:
                return EndpointPatchFilterTypes
        
            @staticmethod
            def channels() -> typing.Type['EndpointPatchChannels']:
                return EndpointPatchChannels
            
            
            class secret(
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
                ) -> 'secret':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def metadata() -> typing.Type['EndpointPatchMetadata']:
                return EndpointPatchMetadata
            __annotations__ = {
                "description": description,
                "version": version,
                "rateLimit": rateLimit,
                "uid": uid,
                "url": url,
                "disabled": disabled,
                "filterTypes": filterTypes,
                "channels": channels,
                "secret": secret,
                "metadata": metadata,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rateLimit"]) -> MetaOapg.properties.rateLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uid"]) -> MetaOapg.properties.uid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disabled"]) -> MetaOapg.properties.disabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filterTypes"]) -> 'EndpointPatchFilterTypes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channels"]) -> 'EndpointPatchChannels': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'EndpointPatchMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "version", "rateLimit", "uid", "url", "disabled", "filterTypes", "channels", "secret", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rateLimit"]) -> typing.Union[MetaOapg.properties.rateLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uid"]) -> typing.Union[MetaOapg.properties.uid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disabled"]) -> typing.Union[MetaOapg.properties.disabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filterTypes"]) -> typing.Union['EndpointPatchFilterTypes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channels"]) -> typing.Union['EndpointPatchChannels', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> typing.Union[MetaOapg.properties.secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['EndpointPatchMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "version", "rateLimit", "uid", "url", "disabled", "filterTypes", "channels", "secret", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        version: typing.Union[MetaOapg.properties.version, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        rateLimit: typing.Union[MetaOapg.properties.rateLimit, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        uid: typing.Union[MetaOapg.properties.uid, None, str, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        disabled: typing.Union[MetaOapg.properties.disabled, bool, schemas.Unset] = schemas.unset,
        filterTypes: typing.Union['EndpointPatchFilterTypes', schemas.Unset] = schemas.unset,
        channels: typing.Union['EndpointPatchChannels', schemas.Unset] = schemas.unset,
        secret: typing.Union[MetaOapg.properties.secret, None, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union['EndpointPatchMetadata', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EndpointPatch':
        return super().__new__(
            cls,
            *args,
            description=description,
            version=version,
            rateLimit=rateLimit,
            uid=uid,
            url=url,
            disabled=disabled,
            filterTypes=filterTypes,
            channels=channels,
            secret=secret,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )

from svix_python_sdk.model.endpoint_patch_channels import EndpointPatchChannels
from svix_python_sdk.model.endpoint_patch_filter_types import EndpointPatchFilterTypes
from svix_python_sdk.model.endpoint_patch_metadata import EndpointPatchMetadata
