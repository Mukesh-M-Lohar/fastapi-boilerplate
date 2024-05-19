from typing import Type, TypeVar
from uuid import UUID

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from core.repository.base import DBOperations

DBOperator = TypeVar("DBOperator", bound=DBOperations)


class CRUDRouter:
    def __init__(
        self,
        service_name: str,
        create_model: Type[BaseModel],
        response_model: Type[BaseModel],
        db_ops: DBOperator,
        **kwargs,
    ):
        self.create_model = create_model
        self.db_ops = db_ops
        self.response_model = response_model
        self.service_name = service_name
        self.router = self.create_router(**kwargs)

    def create_router(self, **kwargs) -> APIRouter:
        router = APIRouter(tags=[f"{self.service_name.upper()}_ROUTE"], **kwargs)

        @router.post(
            f"{self.service_name}/create",
            status_code=status.HTTP_201_CREATED,
        )
        async def create_item(item_data: self.create_model):
            f"""create a new {self.service_name} item"""
            return self.db_ops["save"](item_data)

        @router.get(
            f"{self.service_name}/get_all",
            status_code=status.HTTP_200_OK,
            response_model=list[self.response_model],
        )
        async def get_all_items():
            f"""get all {self.service_name} items"""
            return self.db_ops["get_all"]()

        @router.get(
            f"{self.service_name}/get",
            status_code=status.HTTP_200_OK,
            response_model=self.response_model,
        )
        async def get_item(item_id: str | UUID):
            f""" get item {self.service_name}"""
            return self.db_ops["get_by_id"](item_id)

        @router.put(
            f"{self.service_name}/update",
            status_code=status.HTTP_200_OK,
            response_model=self.response_model,
        )
        async def replace_item(item_id: str | UUID, item_data: dict):
            f"""PUT update {self.service_name}"""
            return self.db_ops["update_by_id"](item_id, params=item_data)

        @router.patch(
            f"{self.service_name}/update",
            status_code=status.HTTP_200_OK,
            response_model=self.response_model,
        )
        async def update_item(item_id: str | UUID, item_data: dict):
            f"""Patch update {self.service_name}"""

            return self.db_ops["update_by_id"](item_id, params=item_data)

        @router.delete(
            f"{self.service_name}/delete", status_code=status.HTTP_202_ACCEPTED
        )
        async def delete_item(item_id: str | UUID):
            f"""delete Item {self.service_name}"""

            if self.db_ops["delete_by_id"](item_id):
                raise HTTPException(
                    detail=f"Deleted item{self.service_name}",
                    status_code=status.HTTP_204_NO_CONTENT,
                )

        return router

    def override_route(self, method: str, route: str, **kwargs):
        """
        Method to override parameters for a specific route.

        Args:
        - method (str): HTTP method for the route (e.g., 'get', 'post', 'put', 'delete').
        - route (str): URL path for the route.
        - **kwargs: Parameters to override for the route.
        """
        route_function = getattr(self.router, method.lower(), None)
        if route_function:
            new_route = route_function(route, **kwargs)
            return new_route
        else:
            raise ValueError(f"Invalid method '{method}' or route '{route}'")

    def unregister_route(self, route: str, method: str):
        """
        Unregister a route from the router.

        Args:
            route (str): The URL path of the route to unregister.
            method (str): The HTTP method of the route to unregister.
        """
        for i, r in enumerate(self.router.routes):
            if r.path == route and r.methods == {method.upper()}:
                self.router.routes.pop(i)
                break
        else:
            raise ValueError(f"Route '{method.upper()} {route}' not found in router.")
