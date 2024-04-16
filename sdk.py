from resources.models import (
    SchemaModel,
    AuthorModel,
    DataModel,
    ProjectModel
)

class IFCExchange:
    def __init__(self):
        pass

    def create_event(
            self,
            author: AuthorModel,
            schema: SchemaModel,
            data: DataModel,
            project: ProjectModel
    ):
        pass

    def publish(self):
        pass

    def get_schema(self):
        pass