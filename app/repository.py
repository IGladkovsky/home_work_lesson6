class OrderRepository:
    def __init__(self):
        self._orders = []
        self._next_order_id = 1

    def get_all(self):
        return self._orders

    def get_by_id(self, order_id):
        for order in self._orders:
            if order['id'] == order_id:
                return order
        return None

    def add(self, order):
        order["id"] = self._next_order_id
        self._orders.append(order)
        self._next_order_id += 1
        return order

    def delete(self, order_id):
        for order in self._orders:
            if order['id'] == order_id:
                self._orders.remove(order)
                return order
        return None

    def update(self, order_id, update_data):
        for order in self._orders:
            if order['id'] == order_id:
                order.update(update_data)
                return order
        return None
