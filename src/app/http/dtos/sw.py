from typing import Text

from pydantic import BaseModel


class PersonResponse(BaseModel):
    name: Text
