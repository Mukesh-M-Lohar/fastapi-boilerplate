from core.helpers.fastapi_helper.base_crud import CRUDRouter
from edusmart.role.db_ops import db_role
from edusmart.role.schema import RoleBase, RoleResponses


def create_role_router():
    router = CRUDRouter(
        service_name="role",
        create_model=RoleBase,
        response_model=RoleResponses,
        db_ops=db_role,
    )
    return router.router
