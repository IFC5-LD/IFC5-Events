from typing import Optional

from cloudevents.http import CloudEvent
from pydantic import BaseModel


class ProjectModel(BaseModel):
    project_name: Optional[str] = None

    @property
    def projectname(self):
        return self.project_name

    @projectname.setter
    def projectname(self, value: str) -> None:
        self.project_name = value

    @projectname.deleter
    def projectname(self) -> str:
        tmp = self.project_name
        self.project_name = None

        return tmp

    def marshal(self) -> dict:
        return {
            "project_name": self.projectname
        }

    @classmethod
    def unmarshal(cls, data: dict):
        """
        unmarshal a dictionary containing the ProjectModel instance's attributes

        :param data:
        """

        return ProjectModel(
            project_name=data.get("project_name", "projectname")
        )