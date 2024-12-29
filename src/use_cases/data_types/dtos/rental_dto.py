from datetime import datetime
from dataclasses import dataclass


@dataclass(slots=True)
class RentalDto:
    rental_id: str = None
    resource_id: str = None
    start_date: datetime = None
    end_date: datetime = None
