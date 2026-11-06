class OrderNotFoundError(Exception):
    def __init__(self, order_id):
        self.order_id=order_id

class OrderAlreadyCompletedError(Exception):
    def __init__(self, order_id):
        self.order_id=order_id