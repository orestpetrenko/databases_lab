from dataclasses import dataclass


@dataclass
class Ticket:
    ticket_id: int
    event_id: int
    seat_id: int
    price: float
    type: str

    def to_dict(self):
        return {
            "ticket_id": self.ticket_id,
            "event_id": self.event_id,
            "seat_id": self.seat_id,
            "price": self.price,
            "type": self.type,
        }
