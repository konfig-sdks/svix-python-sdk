from svix_python_sdk.paths.api_v1_app_app_id.get import ApiForget
from svix_python_sdk.paths.api_v1_app_app_id.put import ApiForput
from svix_python_sdk.paths.api_v1_app_app_id.delete import ApiFordelete
from svix_python_sdk.paths.api_v1_app_app_id.patch import ApiForpatch


class ApiV1AppAppId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
