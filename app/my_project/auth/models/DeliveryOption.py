from dataclasses import dataclass


@dataclass
class DeliveryOption:
    delivery_option_id: int
    type: str
    price: float

    def to_dict(self):
        return {
            "delivery_option_id": self.delivery_option_id,
            "type": self.type,
            "price": self.price,
        }