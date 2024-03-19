# coding: utf-8

"""
    Svix API

    Welcome to the Svix API documentation!  Useful links: [Homepage](https://www.svix.com) | [Support email](mailto:support+docs@svix.com) | [Blog](https://www.svix.com/blog/) | [Slack Community](https://www.svix.com/slack/)  # Introduction  This is the reference documentation and schemas for the [Svix webhook service](https://www.svix.com) API. For tutorials and other documentation please refer to [the documentation](https://docs.svix.com).  ## Main concepts  In Svix you have four important entities you will be interacting with:  - `messages`: these are the webhooks being sent. They can have contents and a few other properties. - `application`: this is where `messages` are sent to. Usually you want to create one application for each user on your platform. - `endpoint`: endpoints are the URLs messages will be sent to. Each application can have multiple `endpoints` and each message sent to that application will be sent to all of them (unless they are not subscribed to the sent event type). - `event-type`: event types are identifiers denoting the type of the message being sent. Event types are primarily used to decide which events are sent to which endpoint.   ## Authentication  Get your authentication token (`AUTH_TOKEN`) from the [Svix dashboard](https://dashboard.svix.com) and use it as part of the `Authorization` header as such: `Authorization: Bearer ${AUTH_TOKEN}`. For more information on authentication, please refer to the [authentication token docs](https://docs.svix.com/api-keys).     ## Code samples  The code samples assume you already have the respective libraries installed and you know how to use them. For the latest information on how to do that, please refer to [the documentation](https://docs.svix.com/).   ## Idempotency  Svix supports [idempotency](https://en.wikipedia.org/wiki/Idempotence) for safely retrying requests without accidentally performing the same operation twice. This is useful when an API call is disrupted in transit and you do not receive a response.  To perform an idempotent request, pass the idempotency key in the `Idempotency-Key` header to the request. The idempotency key should be a unique value generated by the client. You can create the key in however way you like, though we suggest using UUID v4, or any other string with enough entropy to avoid collisions.  Svix's idempotency works by saving the resulting status code and body of the first request made for any given idempotency key for any successful request. Subsequent requests with the same key return the same result for a period of up to 12 hours.  Please note that idempotency is only supported for `POST` requests.   ## Cross-Origin Resource Sharing  This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/). And that allows cross-domain communication from the browser. All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site. 

    The version of the OpenAPI document: 1.21.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from svix_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from svix_python_sdk.api_response import AsyncGeneratorResponse
from svix_python_sdk import api_client, exceptions
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

from svix_python_sdk.model.http_error_out import HttpErrorOut as HttpErrorOutSchema
from svix_python_sdk.model.message_status import MessageStatus as MessageStatusSchema
from svix_python_sdk.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema
from svix_python_sdk.model.list_response_endpoint_message_out import ListResponseEndpointMessageOut as ListResponseEndpointMessageOutSchema

from svix_python_sdk.type.http_error_out import HttpErrorOut
from svix_python_sdk.type.list_response_endpoint_message_out import ListResponseEndpointMessageOut
from svix_python_sdk.type.message_status import MessageStatus
from svix_python_sdk.type.http_validation_error import HTTPValidationError

from ...api_client import Dictionary
from svix_python_sdk.pydantic.http_error_out import HttpErrorOut as HttpErrorOutPydantic
from svix_python_sdk.pydantic.message_status import MessageStatus as MessageStatusPydantic
from svix_python_sdk.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic
from svix_python_sdk.pydantic.list_response_endpoint_message_out import ListResponseEndpointMessageOut as ListResponseEndpointMessageOutPydantic

# Query params


class LimitSchema(
    schemas.IntSchema
):
    pass


class IteratorSchema(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    def __new__(
        cls,
        *args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IteratorSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class ChannelSchema(
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
    ) -> 'ChannelSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class TagSchema(
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
    ) -> 'TagSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
StatusSchema = MessageStatusSchema


class BeforeSchema(
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
    ) -> 'BeforeSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class AfterSchema(
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
    ) -> 'AfterSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
WithContentSchema = schemas.BoolSchema


class EventTypesSchema(
    schemas.ListBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneTupleMixin
):


    class MetaOapg:
        
        
        class items(
            schemas.StrSchema
        ):
            pass


    def __new__(
        cls,
        *args: typing.Union[list, tuple, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EventTypesSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'iterator': typing.Union[IteratorSchema, None, str, ],
        'channel': typing.Union[ChannelSchema, None, str, ],
        'tag': typing.Union[TagSchema, None, str, ],
        'status': typing.Union[StatusSchema, ],
        'before': typing.Union[BeforeSchema, None, str, datetime, ],
        'after': typing.Union[AfterSchema, None, str, datetime, ],
        'with_content': typing.Union[WithContentSchema, bool, ],
        'event_types': typing.Union[EventTypesSchema, list, tuple, None, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_iterator = api_client.QueryParameter(
    name="iterator",
    style=api_client.ParameterStyle.FORM,
    schema=IteratorSchema,
    explode=True,
)
request_query_channel = api_client.QueryParameter(
    name="channel",
    style=api_client.ParameterStyle.FORM,
    schema=ChannelSchema,
    explode=True,
)
request_query_tag = api_client.QueryParameter(
    name="tag",
    style=api_client.ParameterStyle.FORM,
    schema=TagSchema,
    explode=True,
)
request_query_status = api_client.QueryParameter(
    name="status",
    style=api_client.ParameterStyle.FORM,
    schema=MessageStatusSchema,
    explode=True,
)
request_query_before = api_client.QueryParameter(
    name="before",
    style=api_client.ParameterStyle.FORM,
    schema=BeforeSchema,
    explode=True,
)
request_query_after = api_client.QueryParameter(
    name="after",
    style=api_client.ParameterStyle.FORM,
    schema=AfterSchema,
    explode=True,
)
request_query_with_content = api_client.QueryParameter(
    name="with_content",
    style=api_client.ParameterStyle.FORM,
    schema=WithContentSchema,
    explode=True,
)
request_query_event_types = api_client.QueryParameter(
    name="event_types",
    style=api_client.ParameterStyle.FORM,
    schema=EventTypesSchema,
    explode=True,
)
# Path params


class AppIdSchema(
    schemas.StrSchema
):
    pass


class EndpointIdSchema(
    schemas.StrSchema
):
    pass
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'app_id': typing.Union[AppIdSchema, str, ],
        'endpoint_id': typing.Union[EndpointIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_app_id = api_client.PathParameter(
    name="app_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AppIdSchema,
    required=True,
)
request_path_endpoint_id = api_client.PathParameter(
    name="endpoint_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EndpointIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ListResponseEndpointMessageOutSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ListResponseEndpointMessageOut


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ListResponseEndpointMessageOut


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = HttpErrorOutSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: HttpErrorOut


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: HttpErrorOut


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = HttpErrorOutSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: HttpErrorOut


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: HttpErrorOut


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = HttpErrorOutSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: HttpErrorOut


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: HttpErrorOut


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = HttpErrorOutSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: HttpErrorOut


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: HttpErrorOut


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor409ResponseBodyApplicationJson = HttpErrorOutSchema


@dataclass
class ApiResponseFor409(api_client.ApiResponse):
    body: HttpErrorOut


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: HttpErrorOut


_response_for_409 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor409,
    response_cls_async=ApiResponseFor409Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor409ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = HTTPValidationErrorSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: HTTPValidationError


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: HTTPValidationError


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
SchemaFor429ResponseBodyApplicationJson = HttpErrorOutSchema


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: HttpErrorOut


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: HttpErrorOut


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_attempted_messages_mapped_args(
        self,
        app_id: str,
        endpoint_id: str,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[typing.Optional[str]] = None,
        channel: typing.Optional[typing.Optional[str]] = None,
        tag: typing.Optional[typing.Optional[str]] = None,
        status: typing.Optional[MessageStatus] = None,
        before: typing.Optional[typing.Optional[datetime]] = None,
        after: typing.Optional[typing.Optional[datetime]] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Optional[typing.List[str]]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if limit is not None:
            _query_params["limit"] = limit
        if iterator is not None:
            _query_params["iterator"] = iterator
        if channel is not None:
            _query_params["channel"] = channel
        if tag is not None:
            _query_params["tag"] = tag
        if status is not None:
            _query_params["status"] = status
        if before is not None:
            _query_params["before"] = before
        if after is not None:
            _query_params["after"] = after
        if with_content is not None:
            _query_params["with_content"] = with_content
        if event_types is not None:
            _query_params["event_types"] = event_types
        if app_id is not None:
            _path_params["app_id"] = app_id
        if endpoint_id is not None:
            _path_params["endpoint_id"] = endpoint_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _alist_attempted_messages_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List Attempted Messages
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_app_id,
            request_path_endpoint_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_iterator,
            request_query_channel,
            request_query_tag,
            request_query_status,
            request_query_before,
            request_query_after,
            request_query_with_content,
            request_query_event_types,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/app/{app_id}/endpoint/{endpoint_id}/msg',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_attempted_messages_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List Attempted Messages
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_app_id,
            request_path_endpoint_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_iterator,
            request_query_channel,
            request_query_tag,
            request_query_status,
            request_query_before,
            request_query_after,
            request_query_with_content,
            request_query_event_types,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/app/{app_id}/endpoint/{endpoint_id}/msg',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListAttemptedMessagesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_attempted_messages(
        self,
        app_id: str,
        endpoint_id: str,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[typing.Optional[str]] = None,
        channel: typing.Optional[typing.Optional[str]] = None,
        tag: typing.Optional[typing.Optional[str]] = None,
        status: typing.Optional[MessageStatus] = None,
        before: typing.Optional[typing.Optional[datetime]] = None,
        after: typing.Optional[typing.Optional[datetime]] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Optional[typing.List[str]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_attempted_messages_mapped_args(
            app_id=app_id,
            endpoint_id=endpoint_id,
            limit=limit,
            iterator=iterator,
            channel=channel,
            tag=tag,
            status=status,
            before=before,
            after=after,
            with_content=with_content,
            event_types=event_types,
        )
        return await self._alist_attempted_messages_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def list_attempted_messages(
        self,
        app_id: str,
        endpoint_id: str,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[typing.Optional[str]] = None,
        channel: typing.Optional[typing.Optional[str]] = None,
        tag: typing.Optional[typing.Optional[str]] = None,
        status: typing.Optional[MessageStatus] = None,
        before: typing.Optional[typing.Optional[datetime]] = None,
        after: typing.Optional[typing.Optional[datetime]] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Optional[typing.List[str]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_attempted_messages_mapped_args(
            app_id=app_id,
            endpoint_id=endpoint_id,
            limit=limit,
            iterator=iterator,
            channel=channel,
            tag=tag,
            status=status,
            before=before,
            after=after,
            with_content=with_content,
            event_types=event_types,
        )
        return self._list_attempted_messages_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class ListAttemptedMessages(BaseApi):

    async def alist_attempted_messages(
        self,
        app_id: str,
        endpoint_id: str,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[typing.Optional[str]] = None,
        channel: typing.Optional[typing.Optional[str]] = None,
        tag: typing.Optional[typing.Optional[str]] = None,
        status: typing.Optional[MessageStatus] = None,
        before: typing.Optional[typing.Optional[datetime]] = None,
        after: typing.Optional[typing.Optional[datetime]] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Optional[typing.List[str]]] = None,
        validate: bool = False,
        **kwargs,
    ) -> ListResponseEndpointMessageOutPydantic:
        raw_response = await self.raw.alist_attempted_messages(
            app_id=app_id,
            endpoint_id=endpoint_id,
            limit=limit,
            iterator=iterator,
            channel=channel,
            tag=tag,
            status=status,
            before=before,
            after=after,
            with_content=with_content,
            event_types=event_types,
            **kwargs,
        )
        if validate:
            return ListResponseEndpointMessageOutPydantic(**raw_response.body)
        return api_client.construct_model_instance(ListResponseEndpointMessageOutPydantic, raw_response.body)
    
    
    def list_attempted_messages(
        self,
        app_id: str,
        endpoint_id: str,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[typing.Optional[str]] = None,
        channel: typing.Optional[typing.Optional[str]] = None,
        tag: typing.Optional[typing.Optional[str]] = None,
        status: typing.Optional[MessageStatus] = None,
        before: typing.Optional[typing.Optional[datetime]] = None,
        after: typing.Optional[typing.Optional[datetime]] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Optional[typing.List[str]]] = None,
        validate: bool = False,
    ) -> ListResponseEndpointMessageOutPydantic:
        raw_response = self.raw.list_attempted_messages(
            app_id=app_id,
            endpoint_id=endpoint_id,
            limit=limit,
            iterator=iterator,
            channel=channel,
            tag=tag,
            status=status,
            before=before,
            after=after,
            with_content=with_content,
            event_types=event_types,
        )
        if validate:
            return ListResponseEndpointMessageOutPydantic(**raw_response.body)
        return api_client.construct_model_instance(ListResponseEndpointMessageOutPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        app_id: str,
        endpoint_id: str,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[typing.Optional[str]] = None,
        channel: typing.Optional[typing.Optional[str]] = None,
        tag: typing.Optional[typing.Optional[str]] = None,
        status: typing.Optional[MessageStatus] = None,
        before: typing.Optional[typing.Optional[datetime]] = None,
        after: typing.Optional[typing.Optional[datetime]] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Optional[typing.List[str]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_attempted_messages_mapped_args(
            app_id=app_id,
            endpoint_id=endpoint_id,
            limit=limit,
            iterator=iterator,
            channel=channel,
            tag=tag,
            status=status,
            before=before,
            after=after,
            with_content=with_content,
            event_types=event_types,
        )
        return await self._alist_attempted_messages_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        app_id: str,
        endpoint_id: str,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[typing.Optional[str]] = None,
        channel: typing.Optional[typing.Optional[str]] = None,
        tag: typing.Optional[typing.Optional[str]] = None,
        status: typing.Optional[MessageStatus] = None,
        before: typing.Optional[typing.Optional[datetime]] = None,
        after: typing.Optional[typing.Optional[datetime]] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Optional[typing.List[str]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_attempted_messages_mapped_args(
            app_id=app_id,
            endpoint_id=endpoint_id,
            limit=limit,
            iterator=iterator,
            channel=channel,
            tag=tag,
            status=status,
            before=before,
            after=after,
            with_content=with_content,
            event_types=event_types,
        )
        return self._list_attempted_messages_oapg(
            query_params=args.query,
            path_params=args.path,
        )

