from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event:
    event_id: int
    name: str
    date: datetime
    location: str
    artist_id: int

    def to_dict(self):
        return {
            "event_id": self.event_id,
            "name": self.name,
            "date": self.date.isoformat() if self.date else None,
            "location": self.location,
            "artist_id": self.artist_id,  # додаємо artist_id
        }
