# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from svix_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ENDPOINT = "Endpoint"
    MESSAGE_ATTEMPT = "Message Attempt"
    INTEGRATION = "Integration"
    EVENT_TYPE = "Event Type"
    APPLICATION = "Application"
    MESSAGE = "Message"
    AUTHENTICATION = "Authentication"
    BACKGROUND_TASKS = "Background Tasks"
    STATISTICS = "Statistics"
    HEALTH = "Health"
    WEBHOOKS = "Webhooks"
