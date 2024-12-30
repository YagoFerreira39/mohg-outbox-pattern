import datetime
from dataclasses import dataclass

from bson import ObjectId


@dataclass(slots=True)
class RentalEventMessageModel:
    rental_id: str
    topic: str = None
    status: str = None
    id_: ObjectId = None
    timestamp: datetime = None

    def to_send(self) -> dict:
        to_send = {
            "id_": str(self.id_),
            "rental_id": self.rental_id,
            "topic": self.topic,
            "status": self.status,
            "timestamp": datetime.datetime.now(tz=datetime.timezone.utc),
        }

        return to_send
