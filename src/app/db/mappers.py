from src.app.http.dtos.sw import PersonResponse
from .models import Person


def response_to_person(dto: PersonResponse) -> Person:
    return Person(name=dto.name)
