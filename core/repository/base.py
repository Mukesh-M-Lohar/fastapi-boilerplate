from typing import Generic, Type, TypeVar

from sqlalchemy import UUID, delete, select, update

from core.db.session import Base, session
from core.repository.enum import SynchronizeSessionEnum

ModelType = TypeVar("ModelType", bound=Base)


class DBOperations(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_all(self) -> list[ModelType]:
        query = select(self.model)
        return await session.execute(query).scalars().all()

    async def get_by_id(self, id: UUID | str) -> ModelType | None:
        query = select(self.model).where(self.model.id == id)
        return await session.execute(query).scalars().first()

    async def update_by_id(
        self,
        id: UUID | str,
        params: dict,
        synchronize_session: SynchronizeSessionEnum = False,
    ) -> None:
        query = (
            update(self.model)
            .where(self.model.id == id)
            .values(**params)
            .execution_options(synchronize_session=synchronize_session)
        )
        return await session.execute(query).scalars().one()

    async def delete(self, model: ModelType) -> None:
        await session.delete(model)

    async def delete_by_id(
        self,
        id: UUID | str,
        synchronize_session: SynchronizeSessionEnum = False,
    ) -> None:
        query = (
            delete(self.model)
            .where(self.model.id == id)
            .execution_options(synchronize_session=synchronize_session)
        )
        await session.execute(query)

    async def save(self, model: ModelType) -> ModelType:
        saved = await session.add(model)
        return saved
