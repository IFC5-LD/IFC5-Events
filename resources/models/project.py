from cloudevents.http import CloudEvent
from pydantic import BaseModel


class ProjectModel(BaseModel):
    _project_name: str

    @property
    def projectname(self):
        return self._project_name

    @projectname.setter
    def projectname(self, value: str) -> None:
        self._project_name = value

    @projectname.deleter
    def projectname(self) -> str:
        tmp = self._project_name
        self._project_name = None

        return tmp

    def marshal(self) -> dict:
        return {
            "project_name": self._project_name
        }

    def unmarshal(self, event: CloudEvent) -> None:
        attributes = event.attributes()
        self._project_name = attributes['project_name']