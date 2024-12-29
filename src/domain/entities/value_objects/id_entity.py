import uuid
from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class IdEntity:
    __value: UUID

    @property
    def value(self) -> str:
        return self.__value.hex

    def __composite_values__(self) -> tuple[str]:
        return (str(self),)

    @classmethod
    def new_one(cls) -> "IdEntity":
        return IdEntity(uuid.uuid4())

    @classmethod
    def of(cls, id: str) -> "IdEntity":
        return cls(uuid.UUID(hex=id, version=4))

    def __str__(self) -> str:
        return self.__value.hex
