#!/usr/bin/python3
"""State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""