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
        print(self.model.project)
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

    @classmethod
    def unmarshal(cls, data: dict):
        # We likely need some better logic here

        event = IFCEvent(
            source=data['source'],
            type=data['type'],
            entity_id=data['entity_id'],
            component_id=data['component_id']
        )

        event.model.schema=SchemaModel.unmarshal(data)
        event.model.author=AuthorModel.unmarshal(data)
        event.model.data=DataModel.unmarshal(data)
        event.model.project=ProjectModel.unmarshal(data)

        return event

