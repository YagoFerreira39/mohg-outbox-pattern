import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class RentalModel:
    resource_id: str
    start_date: datetime
    end_date: datetime
    created_at: datetime = None
    updated_at: datetime = None
    rental_id: str = None

    def __as_dict(self) -> dict:
        model_dict = {
            "resource_id": self.resource_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }

        return model_dict

    def to_insert(self) -> dict:
        model_to_insert = self.__as_dict()
        model_to_insert["created_at"] = datetime.datetime.now(tz=datetime.timezone.utc)
        model_to_insert["updated_at"] = datetime.datetime.now(tz=datetime.timezone.utc)

        return model_to_insert
