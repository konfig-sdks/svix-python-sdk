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


class TemplatePatch(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            name = schemas.StrSchema
            logo = schemas.StrSchema
        
            @staticmethod
            def kind() -> typing.Type['TransformationTemplateKind']:
                return TransformationTemplateKind
            instructions = schemas.StrSchema
            
            
            class instructionsLink(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uri'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'instructionsLink':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def filterTypes() -> typing.Type['TemplatePatchFilterTypes']:
                return TemplatePatchFilterTypes
            
            
            class transformation(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 51200
                    min_length = 10
            
            
            class featureFlag(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 256
                    regex=[{
                        'pattern': r'^[a-zA-Z0-9\-_.]+$',
                    }]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'featureFlag':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "description": description,
                "name": name,
                "logo": logo,
                "kind": kind,
                "instructions": instructions,
                "instructionsLink": instructionsLink,
                "filterTypes": filterTypes,
                "transformation": transformation,
                "featureFlag": featureFlag,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kind"]) -> 'TransformationTemplateKind': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instructions"]) -> MetaOapg.properties.instructions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instructionsLink"]) -> MetaOapg.properties.instructionsLink: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filterTypes"]) -> 'TemplatePatchFilterTypes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transformation"]) -> MetaOapg.properties.transformation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["featureFlag"]) -> MetaOapg.properties.featureFlag: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "name", "logo", "kind", "instructions", "instructionsLink", "filterTypes", "transformation", "featureFlag", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo"]) -> typing.Union[MetaOapg.properties.logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kind"]) -> typing.Union['TransformationTemplateKind', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instructions"]) -> typing.Union[MetaOapg.properties.instructions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instructionsLink"]) -> typing.Union[MetaOapg.properties.instructionsLink, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filterTypes"]) -> typing.Union['TemplatePatchFilterTypes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transformation"]) -> typing.Union[MetaOapg.properties.transformation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["featureFlag"]) -> typing.Union[MetaOapg.properties.featureFlag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "name", "logo", "kind", "instructions", "instructionsLink", "filterTypes", "transformation", "featureFlag", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        logo: typing.Union[MetaOapg.properties.logo, str, schemas.Unset] = schemas.unset,
        kind: typing.Union['TransformationTemplateKind', schemas.Unset] = schemas.unset,
        instructions: typing.Union[MetaOapg.properties.instructions, str, schemas.Unset] = schemas.unset,
        instructionsLink: typing.Union[MetaOapg.properties.instructionsLink, None, str, schemas.Unset] = schemas.unset,
        filterTypes: typing.Union['TemplatePatchFilterTypes', schemas.Unset] = schemas.unset,
        transformation: typing.Union[MetaOapg.properties.transformation, str, schemas.Unset] = schemas.unset,
        featureFlag: typing.Union[MetaOapg.properties.featureFlag, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TemplatePatch':
        return super().__new__(
            cls,
            *args,
            description=description,
            name=name,
            logo=logo,
            kind=kind,
            instructions=instructions,
            instructionsLink=instructionsLink,
            filterTypes=filterTypes,
            transformation=transformation,
            featureFlag=featureFlag,
            _configuration=_configuration,
            **kwargs,
        )

from svix_python_sdk.model.template_patch_filter_types import TemplatePatchFilterTypes
from svix_python_sdk.model.transformation_template_kind import TransformationTemplateKind
