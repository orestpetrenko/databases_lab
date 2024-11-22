from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Payment:
    payment_id: int
    order_id: int
    amount: float
    payment_method: str
    payment_date: Optional[datetime] = None

    def to_dict(self):
        return {
            "payment_id": self.payment_id,
            "order_id": self.order_id,
            "amount": self.amount,
            "payment_date": self.payment_date.isoformat() if self.payment_date else None,
            "payment_method": self.payment_method,
        }