from fastapi import APIRouter, status, Query
from app.schemas import Order, OrderCreate, OrderUpdate, StatusEnum
from app.dependencies import ServiceDep, PaginationDep
from typing import Optional

router = APIRouter(prefix="/orders", tags=["Заказы"])


@router.post("/", response_model=Order, status_code=status.HTTP_201_CREATED,
             summary="Создание нового заказа")
async def create_order(service: ServiceDep, order: OrderCreate):
    return service.create_order(order.model_dump())


@router.get("/", response_model=list[Order], summary="Получение всех заказов")
async def get_orders(
    service: ServiceDep,
    pagination: PaginationDep,
    status: Optional[StatusEnum] = Query(
        default=None,
        description="Фильтр по статусу заказа",
    ),
):
    return service.get_orders(
        status,
        pagination["limit"],
        pagination["offset"],
    )

@router.get("/{order_id}", response_model=Order, summary="Получение заказа с конкретным id")
async def get_order(service: ServiceDep, order_id: int):
    return service.get_order(order_id)


@router.patch("/{order_id}", response_model=Order, summary="Изменение заказа с конкретным id")
async def patch_order(service: ServiceDep, order_id: int, order_update: OrderUpdate):
    return service.update_order(order_id, order_update.model_dump(exclude_unset=True))


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Удаление заказа")
async def delete_order(service: ServiceDep, order_id: int):
    return service.delete_order(order_id)
