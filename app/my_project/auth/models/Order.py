from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:
    order_id: int
    customer_name: str
    order_date: datetime
    delivery_option_id: int
    payment_status: str

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "order_date": self.order_date.isoformat() if self.order_date else None,
            "delivery_option_id": self.delivery_option_id,
            "payment_status": self.payment_status,
        }