from tinydb import TinyDB

from .user import UserRepository, get_user_repository


class Repository:  # noqa: D101
    user_repository: UserRepository

    def __init__(self, user_repository: UserRepository) -> None:
        """Initialize the repository.

        Args:
            user_repository (UserRepository): The user repository.

        """
        self.user_repository = user_repository


def get_repository(db: TinyDB) -> Repository:
    """Get the repository.

    Returns:
        Repository: repository.

    """
    user_repository = get_user_repository(db=db)
    return Repository(user_repository=user_repository)
