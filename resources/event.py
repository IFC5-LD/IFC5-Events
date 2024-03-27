import datetime
import uuid
from typing import Union, Optional

from cloudevents.pydantic import CloudEvent

from resources.models import EventModel, SchemaModel, AuthorModel, DataModel, ProjectModel


class IFCEvent(CloudEvent):
    source: str
    entity_id: Union[str, int, uuid.UUID]
    component_id: Union[str, int, uuid.UUID]
    model: EventModel = EventModel()

    def marshal(self) -> CloudEvent:
        format = "cloudevent"
        attributes = {
            **self.model.schema.marshal(format),
            **self.model.author.marshal(format),
            **self.model.data.marshal(format),
            **self.model.project.marshal(format)
        }

        payload = self.model.data.data

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

        self.entity_id = data['entity_id']
        self.component_id = data['component_id']
        self.model.schema = SchemaModel(**data['_schema'])
        self.model.author = AuthorModel(**data['_author'])
        self.model.data = DataModel(**data['_data'])
        self.model.project = ProjectModel(**data['_project'])
