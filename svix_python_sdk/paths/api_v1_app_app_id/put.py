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
from svix_python_sdk.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema
from svix_python_sdk.model.application_out import ApplicationOut as ApplicationOutSchema
from svix_python_sdk.model.application_in_metadata import ApplicationInMetadata as ApplicationInMetadataSchema
from svix_python_sdk.model.application_in import ApplicationIn as ApplicationInSchema

from svix_python_sdk.type.http_error_out import HttpErrorOut
from svix_python_sdk.type.application_in_metadata import ApplicationInMetadata
from svix_python_sdk.type.application_out import ApplicationOut
from svix_python_sdk.type.application_in import ApplicationIn
from svix_python_sdk.type.http_validation_error import HTTPValidationError

from ...api_client import Dictionary
from svix_python_sdk.pydantic.http_error_out import HttpErrorOut as HttpErrorOutPydantic
from svix_python_sdk.pydantic.application_in_metadata import ApplicationInMetadata as ApplicationInMetadataPydantic
from svix_python_sdk.pydantic.application_out import ApplicationOut as ApplicationOutPydantic
from svix_python_sdk.pydantic.application_in import ApplicationIn as ApplicationInPydantic
from svix_python_sdk.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic

from . import path

# Path params


class AppIdSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 256
        min_length = 1
        regex=[{
            'pattern': r'^[a-zA-Z0-9\-_.]+$',
        }]
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'app_id': typing.Union[AppIdSchema, str, ],
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
# body param
SchemaForRequestBodyApplicationJson = ApplicationInSchema


request_body_application_in = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'HTTPBearer',
]
SchemaFor200ResponseBodyApplicationJson = ApplicationOutSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ApplicationOut


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ApplicationOut


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = ApplicationOutSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: ApplicationOut


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: ApplicationOut


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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
_status_code_to_response = {
    '200': _response_for_200,
    '201': _response_for_201,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '409': _response_for_409,
    '422': _response_for_422,
    '429': _response_for_429,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_application_by_id_mapped_args(
        self,
        name: str,
        app_id: str,
        rate_limit: typing.Optional[typing.Optional[int]] = None,
        uid: typing.Optional[typing.Optional[str]] = None,
        metadata: typing.Optional[ApplicationInMetadata] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if name is not None:
            _body["name"] = name
        if rate_limit is not None:
            _body["rateLimit"] = rate_limit
        if uid is not None:
            _body["uid"] = uid
        if metadata is not None:
            _body["metadata"] = metadata
        args.body = _body
        if app_id is not None:
            _path_params["app_id"] = app_id
        args.path = _path_params
        return args

    async def _aupdate_application_by_id_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update Application
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_app_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/app/{app_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_application_in.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _update_application_by_id_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update Application
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_app_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/app/{app_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_application_in.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class UpdateApplicationByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_application_by_id(
        self,
        name: str,
        app_id: str,
        rate_limit: typing.Optional[typing.Optional[int]] = None,
        uid: typing.Optional[typing.Optional[str]] = None,
        metadata: typing.Optional[ApplicationInMetadata] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_application_by_id_mapped_args(
            name=name,
            app_id=app_id,
            rate_limit=rate_limit,
            uid=uid,
            metadata=metadata,
        )
        return await self._aupdate_application_by_id_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_application_by_id(
        self,
        name: str,
        app_id: str,
        rate_limit: typing.Optional[typing.Optional[int]] = None,
        uid: typing.Optional[typing.Optional[str]] = None,
        metadata: typing.Optional[ApplicationInMetadata] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_application_by_id_mapped_args(
            name=name,
            app_id=app_id,
            rate_limit=rate_limit,
            uid=uid,
            metadata=metadata,
        )
        return self._update_application_by_id_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateApplicationById(BaseApi):

    async def aupdate_application_by_id(
        self,
        name: str,
        app_id: str,
        rate_limit: typing.Optional[typing.Optional[int]] = None,
        uid: typing.Optional[typing.Optional[str]] = None,
        metadata: typing.Optional[ApplicationInMetadata] = None,
        validate: bool = False,
        **kwargs,
    ) -> ApplicationOutPydantic:
        raw_response = await self.raw.aupdate_application_by_id(
            name=name,
            app_id=app_id,
            rate_limit=rate_limit,
            uid=uid,
            metadata=metadata,
            **kwargs,
        )
        if validate:
            return ApplicationOutPydantic(**raw_response.body)
        return api_client.construct_model_instance(ApplicationOutPydantic, raw_response.body)
    
    
    def update_application_by_id(
        self,
        name: str,
        app_id: str,
        rate_limit: typing.Optional[typing.Optional[int]] = None,
        uid: typing.Optional[typing.Optional[str]] = None,
        metadata: typing.Optional[ApplicationInMetadata] = None,
        validate: bool = False,
    ) -> ApplicationOutPydantic:
        raw_response = self.raw.update_application_by_id(
            name=name,
            app_id=app_id,
            rate_limit=rate_limit,
            uid=uid,
            metadata=metadata,
        )
        if validate:
            return ApplicationOutPydantic(**raw_response.body)
        return api_client.construct_model_instance(ApplicationOutPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        name: str,
        app_id: str,
        rate_limit: typing.Optional[typing.Optional[int]] = None,
        uid: typing.Optional[typing.Optional[str]] = None,
        metadata: typing.Optional[ApplicationInMetadata] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_application_by_id_mapped_args(
            name=name,
            app_id=app_id,
            rate_limit=rate_limit,
            uid=uid,
            metadata=metadata,
        )
        return await self._aupdate_application_by_id_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        name: str,
        app_id: str,
        rate_limit: typing.Optional[typing.Optional[int]] = None,
        uid: typing.Optional[typing.Optional[str]] = None,
        metadata: typing.Optional[ApplicationInMetadata] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_application_by_id_mapped_args(
            name=name,
            app_id=app_id,
            rate_limit=rate_limit,
            uid=uid,
            metadata=metadata,
        )
        return self._update_application_by_id_oapg(
            body=args.body,
            path_params=args.path,
        )

