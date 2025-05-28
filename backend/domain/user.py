from pydantic import BaseModel


class User(BaseModel):
    """User model.

    Attributes:
        id (str): The user ID.
        name (str): The user name.

    """

    id: str
    name: str
