import typing_extensions

from svix_python_sdk.apis.tags import TagValues
from svix_python_sdk.apis.tags.endpoint_api import EndpointApi
from svix_python_sdk.apis.tags.message_attempt_api import MessageAttemptApi
from svix_python_sdk.apis.tags.integration_api import IntegrationApi
from svix_python_sdk.apis.tags.event_type_api import EventTypeApi
from svix_python_sdk.apis.tags.application_api import ApplicationApi
from svix_python_sdk.apis.tags.message_api import MessageApi
from svix_python_sdk.apis.tags.authentication_api import AuthenticationApi
from svix_python_sdk.apis.tags.background_tasks_api import BackgroundTasksApi
from svix_python_sdk.apis.tags.statistics_api import StatisticsApi
from svix_python_sdk.apis.tags.health_api import HealthApi
from svix_python_sdk.apis.tags.webhooks_api import WebhooksApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ENDPOINT: EndpointApi,
        TagValues.MESSAGE_ATTEMPT: MessageAttemptApi,
        TagValues.INTEGRATION: IntegrationApi,
        TagValues.EVENT_TYPE: EventTypeApi,
        TagValues.APPLICATION: ApplicationApi,
        TagValues.MESSAGE: MessageApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.BACKGROUND_TASKS: BackgroundTasksApi,
        TagValues.STATISTICS: StatisticsApi,
        TagValues.HEALTH: HealthApi,
        TagValues.WEBHOOKS: WebhooksApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ENDPOINT: EndpointApi,
        TagValues.MESSAGE_ATTEMPT: MessageAttemptApi,
        TagValues.INTEGRATION: IntegrationApi,
        TagValues.EVENT_TYPE: EventTypeApi,
        TagValues.APPLICATION: ApplicationApi,
        TagValues.MESSAGE: MessageApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.BACKGROUND_TASKS: BackgroundTasksApi,
        TagValues.STATISTICS: StatisticsApi,
        TagValues.HEALTH: HealthApi,
        TagValues.WEBHOOKS: WebhooksApi,
    }
)
