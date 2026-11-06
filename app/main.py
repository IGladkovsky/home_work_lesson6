from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exceptions import OrderNotFoundError, OrderAlreadyCompletedError
from app.routers import orders

app = FastAPI()
app.include_router(orders.router)


@app.exception_handler(OrderNotFoundError)
async def order_not_found_exception_handler(
        request: Request, exc: OrderNotFoundError
):
    return JSONResponse(status_code=404, content={"detail": f"Заказ с id={exc.order_id} не найден"})


@app.exception_handler(OrderAlreadyCompletedError)
async def order_not_found_exception_handler(
        request: Request, exc: OrderAlreadyCompletedError
):
    return JSONResponse(status_code=409,
                        content={"detail": f"Заказ {exc.order_id} уже выполнен и не может быть изменён"})
