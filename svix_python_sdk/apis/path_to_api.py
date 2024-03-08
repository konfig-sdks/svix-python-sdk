import typing_extensions

from svix_python_sdk.paths import PathValues
from svix_python_sdk.apis.paths.api_v1_auth_app_portal_access_app_id import ApiV1AuthAppPortalAccessAppId
from svix_python_sdk.apis.paths.api_v1_auth_dashboard_access_app_id import ApiV1AuthDashboardAccessAppId
from svix_python_sdk.apis.paths.api_v1_auth_logout import ApiV1AuthLogout
from svix_python_sdk.apis.paths.api_v1_auth_app_app_id_expire_all import ApiV1AuthAppAppIdExpireAll
from svix_python_sdk.apis.paths.api_v1_app import ApiV1App
from svix_python_sdk.apis.paths.api_v1_app_app_id import ApiV1AppAppId
from svix_python_sdk.apis.paths.api_v1_app_app_id_endpoint import ApiV1AppAppIdEndpoint
from svix_python_sdk.apis.paths.api_v1_app_app_id_endpoint_endpoint_id import ApiV1AppAppIdEndpointEndpointId
from svix_python_sdk.apis.paths.api_v1_app_app_id_endpoint_endpoint_id_secret import ApiV1AppAppIdEndpointEndpointIdSecret
from svix_python_sdk.apis.paths.api_v1_app_app_id_endpoint_endpoint_id_secret_rotate import ApiV1AppAppIdEndpointEndpointIdSecretRotate
from svix_python_sdk.apis.paths.api_v1_app_app_id_endpoint_endpoint_id_stats import ApiV1AppAppIdEndpointEndpointIdStats
from svix_python_sdk.apis.paths.api_v1_app_app_id_endpoint_endpoint_id_recover import ApiV1AppAppIdEndpointEndpointIdRecover
from svix_python_sdk.apis.paths.api_v1_app_app_id_endpoint_endpoint_id_replay_missing import ApiV1AppAppIdEndpointEndpointIdReplayMissing
from svix_python_sdk.apis.paths.api_v1_app_app_id_endpoint_endpoint_id_headers import ApiV1AppAppIdEndpointEndpointIdHeaders
from svix_python_sdk.apis.paths.api_v1_app_app_id_endpoint_endpoint_id_transformation import ApiV1AppAppIdEndpointEndpointIdTransformation
from svix_python_sdk.apis.paths.api_v1_app_app_id_endpoint_endpoint_id_send_example import ApiV1AppAppIdEndpointEndpointIdSendExample
from svix_python_sdk.apis.paths.api_v1_event_type import ApiV1EventType
from svix_python_sdk.apis.paths.api_v1_event_type_import_openapi import ApiV1EventTypeImportOpenapi
from svix_python_sdk.apis.paths.api_v1_event_type_event_type_name import ApiV1EventTypeEventTypeName
from svix_python_sdk.apis.paths.api_v1_background_task import ApiV1BackgroundTask
from svix_python_sdk.apis.paths.api_v1_background_task_task_id import ApiV1BackgroundTaskTaskId
from svix_python_sdk.apis.paths.api_v1_app_app_id_msg import ApiV1AppAppIdMsg
from svix_python_sdk.apis.paths.api_v1_app_app_id_msg_msg_id import ApiV1AppAppIdMsgMsgId
from svix_python_sdk.apis.paths.api_v1_app_app_id_msg_msg_id_content import ApiV1AppAppIdMsgMsgIdContent
from svix_python_sdk.apis.paths.api_v1_app_app_id_attempt_endpoint_endpoint_id import ApiV1AppAppIdAttemptEndpointEndpointId
from svix_python_sdk.apis.paths.api_v1_app_app_id_attempt_msg_msg_id import ApiV1AppAppIdAttemptMsgMsgId
from svix_python_sdk.apis.paths.api_v1_app_app_id_endpoint_endpoint_id_msg import ApiV1AppAppIdEndpointEndpointIdMsg
from svix_python_sdk.apis.paths.api_v1_app_app_id_msg_msg_id_endpoint import ApiV1AppAppIdMsgMsgIdEndpoint
from svix_python_sdk.apis.paths.api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_attempt import ApiV1AppAppIdMsgMsgIdEndpointEndpointIdAttempt
from svix_python_sdk.apis.paths.api_v1_app_app_id_msg_msg_id_attempt import ApiV1AppAppIdMsgMsgIdAttempt
from svix_python_sdk.apis.paths.api_v1_app_app_id_msg_msg_id_attempt_attempt_id import ApiV1AppAppIdMsgMsgIdAttemptAttemptId
from svix_python_sdk.apis.paths.api_v1_app_app_id_msg_msg_id_attempt_attempt_id_content import ApiV1AppAppIdMsgMsgIdAttemptAttemptIdContent
from svix_python_sdk.apis.paths.api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_resend import ApiV1AppAppIdMsgMsgIdEndpointEndpointIdResend
from svix_python_sdk.apis.paths.api_v1_stats_usage_app import ApiV1StatsUsageApp
from svix_python_sdk.apis.paths.api_v1_stats_usage_event_types import ApiV1StatsUsageEventTypes
from svix_python_sdk.apis.paths.api_v1_app_app_id_integration import ApiV1AppAppIdIntegration
from svix_python_sdk.apis.paths.api_v1_app_app_id_integration_integ_id import ApiV1AppAppIdIntegrationIntegId
from svix_python_sdk.apis.paths.api_v1_app_app_id_integration_integ_id_key import ApiV1AppAppIdIntegrationIntegIdKey
from svix_python_sdk.apis.paths.api_v1_app_app_id_integration_integ_id_key_rotate import ApiV1AppAppIdIntegrationIntegIdKeyRotate
from svix_python_sdk.apis.paths.api_v1_health import ApiV1Health

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V1_AUTH_APPPORTALACCESS_APP_ID: ApiV1AuthAppPortalAccessAppId,
        PathValues.API_V1_AUTH_DASHBOARDACCESS_APP_ID: ApiV1AuthDashboardAccessAppId,
        PathValues.API_V1_AUTH_LOGOUT: ApiV1AuthLogout,
        PathValues.API_V1_AUTH_APP_APP_ID_EXPIREALL: ApiV1AuthAppAppIdExpireAll,
        PathValues.API_V1_APP: ApiV1App,
        PathValues.API_V1_APP_APP_ID: ApiV1AppAppId,
        PathValues.API_V1_APP_APP_ID_ENDPOINT: ApiV1AppAppIdEndpoint,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID: ApiV1AppAppIdEndpointEndpointId,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_SECRET: ApiV1AppAppIdEndpointEndpointIdSecret,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_SECRET_ROTATE: ApiV1AppAppIdEndpointEndpointIdSecretRotate,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_STATS: ApiV1AppAppIdEndpointEndpointIdStats,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_RECOVER: ApiV1AppAppIdEndpointEndpointIdRecover,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_REPLAYMISSING: ApiV1AppAppIdEndpointEndpointIdReplayMissing,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_HEADERS: ApiV1AppAppIdEndpointEndpointIdHeaders,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_TRANSFORMATION: ApiV1AppAppIdEndpointEndpointIdTransformation,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_SENDEXAMPLE: ApiV1AppAppIdEndpointEndpointIdSendExample,
        PathValues.API_V1_EVENTTYPE: ApiV1EventType,
        PathValues.API_V1_EVENTTYPE_IMPORT_OPENAPI: ApiV1EventTypeImportOpenapi,
        PathValues.API_V1_EVENTTYPE_EVENT_TYPE_NAME: ApiV1EventTypeEventTypeName,
        PathValues.API_V1_BACKGROUNDTASK: ApiV1BackgroundTask,
        PathValues.API_V1_BACKGROUNDTASK_TASK_ID: ApiV1BackgroundTaskTaskId,
        PathValues.API_V1_APP_APP_ID_MSG: ApiV1AppAppIdMsg,
        PathValues.API_V1_APP_APP_ID_MSG_MSG_ID: ApiV1AppAppIdMsgMsgId,
        PathValues.API_V1_APP_APP_ID_MSG_MSG_ID_CONTENT: ApiV1AppAppIdMsgMsgIdContent,
        PathValues.API_V1_APP_APP_ID_ATTEMPT_ENDPOINT_ENDPOINT_ID: ApiV1AppAppIdAttemptEndpointEndpointId,
        PathValues.API_V1_APP_APP_ID_ATTEMPT_MSG_MSG_ID: ApiV1AppAppIdAttemptMsgMsgId,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_MSG: ApiV1AppAppIdEndpointEndpointIdMsg,
        PathValues.API_V1_APP_APP_ID_MSG_MSG_ID_ENDPOINT: ApiV1AppAppIdMsgMsgIdEndpoint,
        PathValues.API_V1_APP_APP_ID_MSG_MSG_ID_ENDPOINT_ENDPOINT_ID_ATTEMPT: ApiV1AppAppIdMsgMsgIdEndpointEndpointIdAttempt,
        PathValues.API_V1_APP_APP_ID_MSG_MSG_ID_ATTEMPT: ApiV1AppAppIdMsgMsgIdAttempt,
        PathValues.API_V1_APP_APP_ID_MSG_MSG_ID_ATTEMPT_ATTEMPT_ID: ApiV1AppAppIdMsgMsgIdAttemptAttemptId,
        PathValues.API_V1_APP_APP_ID_MSG_MSG_ID_ATTEMPT_ATTEMPT_ID_CONTENT: ApiV1AppAppIdMsgMsgIdAttemptAttemptIdContent,
        PathValues.API_V1_APP_APP_ID_MSG_MSG_ID_ENDPOINT_ENDPOINT_ID_RESEND: ApiV1AppAppIdMsgMsgIdEndpointEndpointIdResend,
        PathValues.API_V1_STATS_USAGE_APP: ApiV1StatsUsageApp,
        PathValues.API_V1_STATS_USAGE_EVENTTYPES: ApiV1StatsUsageEventTypes,
        PathValues.API_V1_APP_APP_ID_INTEGRATION: ApiV1AppAppIdIntegration,
        PathValues.API_V1_APP_APP_ID_INTEGRATION_INTEG_ID: ApiV1AppAppIdIntegrationIntegId,
        PathValues.API_V1_APP_APP_ID_INTEGRATION_INTEG_ID_KEY: ApiV1AppAppIdIntegrationIntegIdKey,
        PathValues.API_V1_APP_APP_ID_INTEGRATION_INTEG_ID_KEY_ROTATE: ApiV1AppAppIdIntegrationIntegIdKeyRotate,
        PathValues.API_V1_HEALTH: ApiV1Health,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V1_AUTH_APPPORTALACCESS_APP_ID: ApiV1AuthAppPortalAccessAppId,
        PathValues.API_V1_AUTH_DASHBOARDACCESS_APP_ID: ApiV1AuthDashboardAccessAppId,
        PathValues.API_V1_AUTH_LOGOUT: ApiV1AuthLogout,
        PathValues.API_V1_AUTH_APP_APP_ID_EXPIREALL: ApiV1AuthAppAppIdExpireAll,
        PathValues.API_V1_APP: ApiV1App,
        PathValues.API_V1_APP_APP_ID: ApiV1AppAppId,
        PathValues.API_V1_APP_APP_ID_ENDPOINT: ApiV1AppAppIdEndpoint,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID: ApiV1AppAppIdEndpointEndpointId,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_SECRET: ApiV1AppAppIdEndpointEndpointIdSecret,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_SECRET_ROTATE: ApiV1AppAppIdEndpointEndpointIdSecretRotate,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_STATS: ApiV1AppAppIdEndpointEndpointIdStats,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_RECOVER: ApiV1AppAppIdEndpointEndpointIdRecover,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_REPLAYMISSING: ApiV1AppAppIdEndpointEndpointIdReplayMissing,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_HEADERS: ApiV1AppAppIdEndpointEndpointIdHeaders,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_TRANSFORMATION: ApiV1AppAppIdEndpointEndpointIdTransformation,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_SENDEXAMPLE: ApiV1AppAppIdEndpointEndpointIdSendExample,
        PathValues.API_V1_EVENTTYPE: ApiV1EventType,
        PathValues.API_V1_EVENTTYPE_IMPORT_OPENAPI: ApiV1EventTypeImportOpenapi,
        PathValues.API_V1_EVENTTYPE_EVENT_TYPE_NAME: ApiV1EventTypeEventTypeName,
        PathValues.API_V1_BACKGROUNDTASK: ApiV1BackgroundTask,
        PathValues.API_V1_BACKGROUNDTASK_TASK_ID: ApiV1BackgroundTaskTaskId,
        PathValues.API_V1_APP_APP_ID_MSG: ApiV1AppAppIdMsg,
        PathValues.API_V1_APP_APP_ID_MSG_MSG_ID: ApiV1AppAppIdMsgMsgId,
        PathValues.API_V1_APP_APP_ID_MSG_MSG_ID_CONTENT: ApiV1AppAppIdMsgMsgIdContent,
        PathValues.API_V1_APP_APP_ID_ATTEMPT_ENDPOINT_ENDPOINT_ID: ApiV1AppAppIdAttemptEndpointEndpointId,
        PathValues.API_V1_APP_APP_ID_ATTEMPT_MSG_MSG_ID: ApiV1AppAppIdAttemptMsgMsgId,
        PathValues.API_V1_APP_APP_ID_ENDPOINT_ENDPOINT_ID_MSG: ApiV1AppAppIdEndpointEndpointIdMsg,
        PathValues.API_V1_APP_APP_ID_MSG_MSG_ID_ENDPOINT: ApiV1AppAppIdMsgMsgIdEndpoint,
        PathValues.API_V1_APP_APP_ID_MSG_MSG_ID_ENDPOINT_ENDPOINT_ID_ATTEMPT: ApiV1AppAppIdMsgMsgIdEndpointEndpointIdAttempt,
        PathValues.API_V1_APP_APP_ID_MSG_MSG_ID_ATTEMPT: ApiV1AppAppIdMsgMsgIdAttempt,
        PathValues.API_V1_APP_APP_ID_MSG_MSG_ID_ATTEMPT_ATTEMPT_ID: ApiV1AppAppIdMsgMsgIdAttemptAttemptId,
        PathValues.API_V1_APP_APP_ID_MSG_MSG_ID_ATTEMPT_ATTEMPT_ID_CONTENT: ApiV1AppAppIdMsgMsgIdAttemptAttemptIdContent,
        PathValues.API_V1_APP_APP_ID_MSG_MSG_ID_ENDPOINT_ENDPOINT_ID_RESEND: ApiV1AppAppIdMsgMsgIdEndpointEndpointIdResend,
        PathValues.API_V1_STATS_USAGE_APP: ApiV1StatsUsageApp,
        PathValues.API_V1_STATS_USAGE_EVENTTYPES: ApiV1StatsUsageEventTypes,
        PathValues.API_V1_APP_APP_ID_INTEGRATION: ApiV1AppAppIdIntegration,
        PathValues.API_V1_APP_APP_ID_INTEGRATION_INTEG_ID: ApiV1AppAppIdIntegrationIntegId,
        PathValues.API_V1_APP_APP_ID_INTEGRATION_INTEG_ID_KEY: ApiV1AppAppIdIntegrationIntegIdKey,
        PathValues.API_V1_APP_APP_ID_INTEGRATION_INTEG_ID_KEY_ROTATE: ApiV1AppAppIdIntegrationIntegIdKeyRotate,
        PathValues.API_V1_HEALTH: ApiV1Health,
    }
)
