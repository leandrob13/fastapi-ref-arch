from factory import Factory, BUILD_STRATEGY

from src.app.http.dtos.sw import PersonResponse


class PersonResponseFactory(Factory):
    class Meta:
        model = PersonResponse
        strategy = BUILD_STRATEGY

    name = "Luke"
