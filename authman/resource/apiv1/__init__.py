from authman.authman import apiv1 as api
from authman.resource.apiv1.user import UserResource

api.add_resource(
    UserResource,
    "/users",
    methods=["GET","POST"],
    endpoint="users"
)
api.add_resource(
    UserResource,
    "/users/<user_id>",
    methods=["GET","PATCH","DELETE"],
    endpoint="user"
)