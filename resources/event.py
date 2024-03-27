import datetime
import uuid
from typing import Union, Optional

from cloudevents.pydantic import CloudEvent

from resources.models import EventModel, SchemaModel, AuthorModel, DataModel, ProjectModel


class IFCEvent(CloudEvent):
    source: str
    entityid: Union[str, int, uuid.UUID]
    componentid: Union[str, int, uuid.UUID]
    model: Optional[EventModel] = EventModel()

    def marshal(self) -> CloudEvent:
        attributes = {
            **self.model.schema.marshal(),
            **self.model.author.marshal(),
            **self.model.data.marshal(),
            **self.model.project.marshal()
        }

        attributes = {}
        payload = self.model.data.marshal()

        return CloudEvent(
            source=self.source,
            type=self.type,
            data=payload,
            datacontenttype="application/cloudevents+json",
            time=str(datetime.datetime.utcnow()),
            **attributes
        )

    def unmarshal(self, event: CloudEvent) -> None:
        # We likely need some better logic here
        attributes = event.attributes()
        data = event.data

        self.source = attributes['source']


        self.entityid = data['entityid']
        self.componentid = data['componentid']
        self.model.schema = SchemaModel(**data['_schema'])
        self.model.author = AuthorModel(**data['_author'])
        self.model.data = DataModel(**data['_data'])
        self.model.project = ProjectModel(**data['_project'])
