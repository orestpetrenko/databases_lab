from dataclasses import dataclass


@dataclass
class Seat:
    seat_id: int
    venue_id: int
    seat_number: str
    is_available: bool

    def to_dict(self):
        return {
            "seat_id": self.seat_id,
            "venue_id": self.venue_id,
            "seat_number": self.seat_number,
            "is_available": self.is_available,
        }