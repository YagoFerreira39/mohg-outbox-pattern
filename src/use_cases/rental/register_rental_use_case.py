from witch_doctor import WitchDoctor

from src.adapters.extensions.exceptions.extension_base_exception import (
    ExtensionBaseException,
)
from src.adapters.repositories.exceptions.repository_base_exception import (
    RepositoryBaseException,
)
from src.domain.entities.rental_entity import RentalEntity
from src.domain.exceptions.entity_base_exception import EntityBaseException
from src.domain.models.rental_model import RentalModel
from src.use_cases.data_types.dtos.register_rental_dto import RegisterRentalDto
from src.use_cases.data_types.requests.register_rental_request import (
    RegisterRentalRequest,
)
from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException
from src.use_cases.exceptions.use_case_exceptions import (
    MalformedRequestInputException,
    UnableToRegisterRentalException,
    UnexpectedUseCaseException,
)
from src.use_cases.ports.extensions.i_register_rental_extension import (
    IRegisterRentalExtension,
)
from src.use_cases.ports.extensions.i_rental_extension import IRentalExtension
from src.use_cases.ports.use_cases.rental.i_register_rental_use_case import (
    IRegisterRentalUseCase,
)


class RegisterRentalUseCase(IRegisterRentalUseCase):
    __rental_extension: IRentalExtension
    __register_rental_extension: IRegisterRentalExtension
    # __rental_repository: IUserRepository

    @WitchDoctor.injection
    def __init__(
        self,
        rental_extension: IRentalExtension,
        register_rental_extension: IRegisterRentalExtension,
        # rental_repository: IUserRepository,
    ):
        RegisterRentalUseCase.__rental_extension = rental_extension
        RegisterRentalUseCase.__register_rental_extension = register_rental_extension
        # RegisterRentalUseCase.__rental_repository = rental_repository

    @classmethod
    async def register_rental(cls, request: RegisterRentalRequest) -> RegisterRentalDto:
        try:
            entity = cls.__create_rental_entity(request=request)

            model = cls.__create_rental_model(entity=entity)

            inserted_model = await cls.__insert_user(model=model)

            dto = cls.__create_user_dto(model=inserted_model)

            return dto

        except UseCaseBaseException as original_exception:
            raise original_exception

        except Exception as original_exception:
            raise UnexpectedUseCaseException(
                message="An unexpected error occurred.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    def __create_rental_entity(cls, request: RegisterRentalRequest) -> RentalEntity:
        try:
            entity = cls.__register_rental_extension.from_request_to_entity(
                request=request
            )

            return entity

        except EntityBaseException as original_exception:
            raise MalformedRequestInputException(
                message=original_exception.message,
                original_error=original_exception.original_error,
            ) from original_exception
        except ExtensionBaseException as original_exception:
            raise UnableToRegisterRentalException(
                message="unable to register rental",
                original_error=original_exception.original_error,
            ) from original_exception

    @classmethod
    def __create_rental_model(cls, entity: RentalEntity) -> RentalModel:
        try:
            model = cls.__register_rental_extension.from_entity_to_model(entity=entity)

            return model

        except ExtensionBaseException as original_exception:
            raise UnableToRegisterRentalException(
                message="unable to register rental",
                original_error=original_exception.original_error,
            ) from original_exception

    @classmethod
    async def __insert_user(cls, model: RentalModel) -> RentalModel:
        try:
            # inserted_model = await cls.__rental_repository.register_user(model=model)

            return model

        except RepositoryBaseException as original_exception:
            raise UnableToRegisterRentalException(
                message="unable to register rental",
                original_error=original_exception.original_error,
            ) from original_exception

    @classmethod
    def __create_user_dto(cls, model: RentalModel) -> RegisterRentalDto:
        try:
            dto = cls.__register_rental_extension.create_dto(registered=bool(model))

            return dto

        except ExtensionBaseException as original_exception:
            raise UnableToRegisterRentalException(
                message="Rental registered, but with errors.",
                original_error=original_exception.original_error,
            ) from original_exception
