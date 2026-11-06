from functools import lru_cache
from fastapi import Depends, Query
from typing import Annotated, Optional
from app.repository import OrderRepository
from app.config import Settings, get_settings
from app.service import OrderService


@lru_cache
def get_repository() -> OrderRepository:
    return OrderRepository()


def get_service(repository: Annotated[OrderRepository, Depends(get_repository)]) -> OrderService:
    return OrderService(repository)


SettingsDep = Annotated[Settings, Depends(get_settings)]


def pagination_params(
    settings: SettingsDep,
    limit: Optional[int] = Query(
        default=None,
        ge=1,
        le=100,
        description="Максимальное количество заказов в ответе",
    ),
    offset: Optional[int] = Query(
        default=None,
        ge=0,
        description="Сколько заказов пропустить в начале",
    ),
) -> dict:
    return {
        "limit": limit if limit is not None else settings.default_page_limit,
        "offset": offset if offset is not None else settings.default_page_offset,
    }

ServiceDep = Annotated[OrderService, Depends(get_service)]
PaginationDep = Annotated[dict, Depends(pagination_params)]
