from core.helpers.fastapi_helper.base_crud import CRUDRouter
from edusmart.user.db_ops import db_user
from edusmart.user.schema import UserBaseModel, UserResponses


def create_user_router():
    router = CRUDRouter(
        service_name="user",
        create_model=UserBaseModel,
        response_model=UserResponses,
        db_ops=db_user,
    )

    return router.router
