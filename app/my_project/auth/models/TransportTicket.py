from dataclasses import dataclass
from datetime import datetime



@dataclass
class TransportTicket:
    transport_ticket_id: int
    order_id: int
    transport_type: str
    departure_date: datetime
    price: float

    def to_dict(self):
        return {
            "transport_ticket_id": self.transport_ticket_id,
            "order_id": self.order_id,
            "transport_type": self.transport_type,
            "departure_date": self.departure_date.isoformat() if self.departure_date else None,
            "price": self.price,
        }