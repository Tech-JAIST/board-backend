from tinydb import Query, TinyDB

from backend.domain import User


class UserRepository:  # noqa: D101
    db: TinyDB

    def __init__(self, db: TinyDB) -> None:
        """Initialize the user repository.

        Args:
            db (TinyDB): The database.

        """
        self.db = db
        if not self.db.contains(Query().name == "root"):
            db.insert({"name": "root", "id": "0d9a2f49-99aa-49e6-bcf6-b123953aca63"})

    def get_users(self) -> list[User]:
        """Get all users.

        Returns:
            list: The list of users.

        """
        user = Query()
        users = self.db.search(user.name.exists())
        return [User(**user) for user in users]


def get_user_repository(db: TinyDB) -> UserRepository:
    """Get the user repository.

    Returns:
        UserRepository: The user repository.

    """
    return UserRepository(db=db)
