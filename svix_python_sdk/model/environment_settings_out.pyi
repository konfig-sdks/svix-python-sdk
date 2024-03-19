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


class EnvironmentSettingsOut(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class customColor(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'color'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'customColor':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class customLogoUrl(
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
                ) -> 'customLogoUrl':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class customFontFamily(
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
                ) -> 'customFontFamily':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class customFontFamilyUrl(
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
                ) -> 'customFontFamilyUrl':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def customThemeOverride() -> typing.Type['CustomThemeOverride']:
                return CustomThemeOverride
            
            
            class displayName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'displayName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            enableChannels = schemas.BoolSchema
            enableMessageTags = schemas.BoolSchema
            enableIntegrationManagement = schemas.BoolSchema
            enableTransformations = schemas.BoolSchema
        
            @staticmethod
            def colorPaletteLight() -> typing.Type['CustomColorPalette']:
                return CustomColorPalette
        
            @staticmethod
            def colorPaletteDark() -> typing.Type['CustomColorPalette']:
                return CustomColorPalette
            showUseSvixPlay = schemas.BoolSchema
            __annotations__ = {
                "customColor": customColor,
                "customLogoUrl": customLogoUrl,
                "customFontFamily": customFontFamily,
                "customFontFamilyUrl": customFontFamilyUrl,
                "customThemeOverride": customThemeOverride,
                "displayName": displayName,
                "enableChannels": enableChannels,
                "enableMessageTags": enableMessageTags,
                "enableIntegrationManagement": enableIntegrationManagement,
                "enableTransformations": enableTransformations,
                "colorPaletteLight": colorPaletteLight,
                "colorPaletteDark": colorPaletteDark,
                "showUseSvixPlay": showUseSvixPlay,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customColor"]) -> MetaOapg.properties.customColor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customLogoUrl"]) -> MetaOapg.properties.customLogoUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFontFamily"]) -> MetaOapg.properties.customFontFamily: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFontFamilyUrl"]) -> MetaOapg.properties.customFontFamilyUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customThemeOverride"]) -> 'CustomThemeOverride': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enableChannels"]) -> MetaOapg.properties.enableChannels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enableMessageTags"]) -> MetaOapg.properties.enableMessageTags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enableIntegrationManagement"]) -> MetaOapg.properties.enableIntegrationManagement: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enableTransformations"]) -> MetaOapg.properties.enableTransformations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["colorPaletteLight"]) -> 'CustomColorPalette': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["colorPaletteDark"]) -> 'CustomColorPalette': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["showUseSvixPlay"]) -> MetaOapg.properties.showUseSvixPlay: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["customColor", "customLogoUrl", "customFontFamily", "customFontFamilyUrl", "customThemeOverride", "displayName", "enableChannels", "enableMessageTags", "enableIntegrationManagement", "enableTransformations", "colorPaletteLight", "colorPaletteDark", "showUseSvixPlay", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customColor"]) -> typing.Union[MetaOapg.properties.customColor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customLogoUrl"]) -> typing.Union[MetaOapg.properties.customLogoUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFontFamily"]) -> typing.Union[MetaOapg.properties.customFontFamily, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFontFamilyUrl"]) -> typing.Union[MetaOapg.properties.customFontFamilyUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customThemeOverride"]) -> typing.Union['CustomThemeOverride', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enableChannels"]) -> typing.Union[MetaOapg.properties.enableChannels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enableMessageTags"]) -> typing.Union[MetaOapg.properties.enableMessageTags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enableIntegrationManagement"]) -> typing.Union[MetaOapg.properties.enableIntegrationManagement, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enableTransformations"]) -> typing.Union[MetaOapg.properties.enableTransformations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["colorPaletteLight"]) -> typing.Union['CustomColorPalette', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["colorPaletteDark"]) -> typing.Union['CustomColorPalette', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["showUseSvixPlay"]) -> typing.Union[MetaOapg.properties.showUseSvixPlay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["customColor", "customLogoUrl", "customFontFamily", "customFontFamilyUrl", "customThemeOverride", "displayName", "enableChannels", "enableMessageTags", "enableIntegrationManagement", "enableTransformations", "colorPaletteLight", "colorPaletteDark", "showUseSvixPlay", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        customColor: typing.Union[MetaOapg.properties.customColor, None, str, schemas.Unset] = schemas.unset,
        customLogoUrl: typing.Union[MetaOapg.properties.customLogoUrl, None, str, schemas.Unset] = schemas.unset,
        customFontFamily: typing.Union[MetaOapg.properties.customFontFamily, None, str, schemas.Unset] = schemas.unset,
        customFontFamilyUrl: typing.Union[MetaOapg.properties.customFontFamilyUrl, None, str, schemas.Unset] = schemas.unset,
        customThemeOverride: typing.Union['CustomThemeOverride', schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, None, str, schemas.Unset] = schemas.unset,
        enableChannels: typing.Union[MetaOapg.properties.enableChannels, bool, schemas.Unset] = schemas.unset,
        enableMessageTags: typing.Union[MetaOapg.properties.enableMessageTags, bool, schemas.Unset] = schemas.unset,
        enableIntegrationManagement: typing.Union[MetaOapg.properties.enableIntegrationManagement, bool, schemas.Unset] = schemas.unset,
        enableTransformations: typing.Union[MetaOapg.properties.enableTransformations, bool, schemas.Unset] = schemas.unset,
        colorPaletteLight: typing.Union['CustomColorPalette', schemas.Unset] = schemas.unset,
        colorPaletteDark: typing.Union['CustomColorPalette', schemas.Unset] = schemas.unset,
        showUseSvixPlay: typing.Union[MetaOapg.properties.showUseSvixPlay, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EnvironmentSettingsOut':
        return super().__new__(
            cls,
            *args,
            customColor=customColor,
            customLogoUrl=customLogoUrl,
            customFontFamily=customFontFamily,
            customFontFamilyUrl=customFontFamilyUrl,
            customThemeOverride=customThemeOverride,
            displayName=displayName,
            enableChannels=enableChannels,
            enableMessageTags=enableMessageTags,
            enableIntegrationManagement=enableIntegrationManagement,
            enableTransformations=enableTransformations,
            colorPaletteLight=colorPaletteLight,
            colorPaletteDark=colorPaletteDark,
            showUseSvixPlay=showUseSvixPlay,
            _configuration=_configuration,
            **kwargs,
        )

from svix_python_sdk.model.custom_color_palette import CustomColorPalette
from svix_python_sdk.model.custom_theme_override import CustomThemeOverride
