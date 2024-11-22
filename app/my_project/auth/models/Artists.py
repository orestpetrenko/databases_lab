from dataclasses import dataclass
from typing import Optional

@dataclass
class Artist:
    artist_id: int
    name: str
    genre: Optional[str] = None
    country: Optional[str] = None

    def to_dict(self):
        return {
            "artist_id": self.artist_id,
            "name": self.name,
            "genre": self.genre,
            "country": self.country,
        }