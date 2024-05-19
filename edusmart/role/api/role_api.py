from uuid import UUID

from fastapi import APIRouter, status

from core.helpers.fastapi_helper.base_crud import CRUDRouter
from edusmart.role.db_ops import db_role
from edusmart.role.schema import RoleBase, RoleResponses, roleBaseModel, roleResponses


def create_role_router(**kwargs):
    router = APIRouter(tags=["Role Router"], **kwargs)

    @router.post(
        "/role",
        status_code=status.HTTP_201_CREATED,
    )
    async def create_role(role_data: RoleBase):
        return db_role.save(role_data)

    @router.get(
        "/roles", status_code=status.HTTP_200_OK, response_model=list[RoleResponses]
    )
    async def get_roles():
        return db_role.get_all()

    @router.get("/role", status_code=status.HTTP_200_OK, response_model=RoleResponses)
    async def get_role(role_id: str):
        return db_role.get_by_id(role_id)

    @router.put("/role", status_code=status.HTTP_200_OK, response_model=RoleResponses)
    async def update_role(role_id: str | UUID, role_data: dict):
        return db_role.update_by_id(role_id, params=role_data)

    @router.delete(
        "/role",
        status_code=status.HTTP_202_ACCEPTED,
    )
    async def delete_role(role_id: str | UUID):
        return db_role.delete_by_id(role_id)

    return router


def create_user_router():
    router = CRUDRouter(
        service_name="role",
        create_model=roleBaseModel,
        response_model=roleResponses,
        db_ops=db_role,
    )
    return router.router
