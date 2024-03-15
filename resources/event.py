import datetime
import uuid

from cloudevents.pydantic import CloudEvent
from typing import Union

from resources.models import EventModel

# Dummy change
class IFCEvent(CloudEvent):
    source: str
    entityid: Union[str, int, uuid.UUID]
    componentid: Union[str, int, uuid.UUID]
    _ifc_event_model: EventModel

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
        self._project = ProjectModel(**data['_project'])