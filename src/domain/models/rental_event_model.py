import datetime
from dataclasses import dataclass

from bson import ObjectId


@dataclass(slots=True)
class RentalEventModel:
    rental_id: str
    topic: str = None
    status: str = None
    id_: ObjectId = None
    created_at: datetime = None
    updated_at: datetime = None

    def __as_dict(self) -> dict:
        model_dict = {
            "rental_id": self.rental_id,
        }

        return model_dict

    def to_insert(self) -> dict:
        model_to_insert = self.__as_dict()
        model_to_insert["topic"] = "rental_topic"
        model_to_insert["status"] = "pending"
        model_to_insert["created_at"] = datetime.datetime.now(tz=datetime.timezone.utc)
        model_to_insert["updated_at"] = datetime.datetime.now(tz=datetime.timezone.utc)

        return model_to_insert
