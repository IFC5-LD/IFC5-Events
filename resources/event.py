import datetime
import uuid

from cloudevents.pydantic import CloudEvent
from typing import Union

from resources.models.author import AuthorModel
from resources.models.data import DataModel
from resources.models.project import ProjectInformation
from resources.models.schema import SchemaModel

# Dummy change
class EventModel(CloudEvent):
    source: str
    entityid: Union[str, int, uuid.UUID]
    componentid: Union[str, int, uuid.UUID]
    _schema: SchemaModel
    _author: AuthorModel
    _data: DataModel
    _project: ProjectInformation

    def __init__(
            self,
            entityid: Union[str],
            componentid: Union[str],
            schema: SchemaModel,
            author: AuthorModel,
            data: DataModel,
            project: ProjectInformation
    ):
        self.entityid = entityid
        self.componentid = componentid
        self._schema = schema
        self._author = author
        self._data = data
        self._project = project

    def marshal(self) -> CloudEvent:

        attributes = {
            **self._schema.marshal(),
            **self._author.marshal(),
            **self._data.marshal(),
            **self._project.marshal()
        }

        data = self._data.data

        return CloudEvent(
            source="https://example.com",
            type="com.example.test",
            data=data,
            datacontenttype="application/cloudevents+json",
            time=str(datetime.datetime.utcnow()),
            **attributes
        )

    def unmarshal(self, data: dict) -> None:
        # We likely need some better logic here
        self.entityid = data['entityid']
        self.componentid = data['componentid']
        self._schema = SchemaModel(**data['_schema'])
        self._author = AuthorModel(**data['_author'])
        self._data = DataModel(**data['_data'])
        self._project = ProjectInformation(**data['_project'])