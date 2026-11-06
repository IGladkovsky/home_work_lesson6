from app.repository import OrderRepository
from app.exceptions import OrderNotFoundError, OrderAlreadyCompletedError
from app.schemas import StatusEnum
from datetime import datetime


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def get_orders(self, status, limit, offset):
        orders = self.repository.get_all()
        if status is not None:
            orders = [o for o in orders if o["status"] == status]
        return orders[offset: offset + limit]

    def get_order(self, order_id):
        if self.repository.get_by_id(order_id) is None:
            raise OrderNotFoundError(order_id)
        return self.repository.get_by_id(order_id)

    def create_order(self, order):
        order.setdefault("status", StatusEnum.PENDING)
        order.setdefault("created_at", datetime.now().replace(microsecond=0))
        return self.repository.add(order)

    def delete_order(self, order_id):
        if self.repository.get_by_id(order_id) is None:
            raise OrderNotFoundError(order_id)
        if self.repository.get_by_id(order_id)["status"] == StatusEnum.COMPLETED:
            raise OrderAlreadyCompletedError(order_id)
        return self.repository.delete(order_id)

    def update_order(self, order_id, order):
        if self.repository.get_by_id(order_id) is None:
            raise OrderNotFoundError(order_id)
        if self.repository.get_by_id(order_id)["status"] == StatusEnum.COMPLETED:
            raise OrderAlreadyCompletedError(order_id)
        return self.repository.update(order_id, order)

    def count_orders(self):
        orders = self.repository.get_all()
        return len(orders)