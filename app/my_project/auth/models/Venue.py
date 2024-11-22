from dataclasses import dataclass


@dataclass
class Venue:
    venue_id: int
    name: str
    address: str
    capacity: int

    def to_dict(self):
        return {
            "venue_id": self.venue_id,
            "name": self.name,
            "address": self.address,
            "capacity": self.capacity,
        }
