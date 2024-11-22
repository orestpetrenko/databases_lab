from dataclasses import dataclass


@dataclass
class OrderedTicket:
    ordered_ticket_id: int
    order_id: int
    ticket_id: int
    quantity: int

    def to_dict(self):
        return {
            "ordered_ticket_id": self.ordered_ticket_id,
            "order_id": self.order_id,
            "ticket_id": self.ticket_id,
            "quantity": self.quantity,
        }
