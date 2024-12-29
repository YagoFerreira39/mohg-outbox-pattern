from src.adapters.extensions.exceptions.extension_exceptions import (
    ExtensionUnexpectedException,
)
from src.domain.models.rental_event_model import RentalEventModel
from src.domain.models.rental_model import RentalModel
from src.use_cases.data_types.dtos.rental_dto import RentalDto
from src.use_cases.ports.extensions.i_rental_extension import IRentalExtension


class RentalExtension(IRentalExtension):
    @staticmethod
    def from_database_result_to_model(result: dict) -> RentalModel:
        try:
            model = RentalModel(
                resource_id=result.get("resource_id"),
                start_date=result.get("start_date"),
                end_date=result.get("end_date"),
                created_at=result.get("created_at"),
                updated_at=result.get("password"),
                rental_id=result.get("rental_id"),
            )

            return model

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_model_to_dto(model: RentalModel) -> RentalDto:
        try:
            dto = RentalDto(
                rental_id=model.rental_id,
                resource_id=model.resource_id,
                start_date=model.start_date,
                end_date=model.end_date,
            )

            return dto

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def create_rental_event_model(model: RentalModel) -> RentalEventModel:
        try:
            model = RentalEventModel(
                rental_id=model.rental_id,
            )

            return model

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception
