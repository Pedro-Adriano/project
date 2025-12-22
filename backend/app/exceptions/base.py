class DomainError(Exception):

    def __init__(
        self,
        message: str = "Ocorreu um erro inesperado no domínio!",
    ) -> None:
        self.message = message
        super().__init__(self.message)


class InfraError(Exception):
    def __init__(
        self,
        code: int = 500,
        message: str = "Ocorreu um erro inesperado na infra",
    ) -> None:
        self.code = code
        self.message = message
        super().__init__(self.message)


class RequiresAuthError(InfraError):
    def __init__(
        self,
        message: str = "Requer autenticação",
    ) -> None:
        super().__init__(401, message)


class ForbiddenError(InfraError):
    def __init__(
        self,
        message: str = "Acesso proibido",
    ) -> None:
        super().__init__(403, message)


class UserNotAuthorizedError(DomainError):
    def __init__(self, message: str = "Usuário não autorizado!") -> None:
        super().__init__(message)


class EntityNotFoundError(DomainError):

    def __init__(self, message: str = "Entidade não encontrada!") -> None:
        super().__init__(message)


class CustomValidationError(DomainError):

    def __init__(
        self,
        message: str = "A entidade possui campos inválidos!",
    ) -> None:
        super().__init__(message)


class InvalidFieldError(DomainError):
    def __init__(self, field: str) -> None:
        self.message = f"O campo {field} é invalido!"
        super().__init__(self.message)


class RequiredFieldError(DomainError):
    def __init__(self, field: str) -> None:
        self.message = f"Campo necessário: {field}!"
        super().__init__(self.message)
