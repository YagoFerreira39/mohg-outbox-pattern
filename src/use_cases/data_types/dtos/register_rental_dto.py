from dataclasses import dataclass


@dataclass(slots=True)
class RegisterRentalDto:
    registered: bool = None
