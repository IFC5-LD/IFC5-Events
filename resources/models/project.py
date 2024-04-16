from typing import Optional

from cloudevents.http import CloudEvent
from pydantic import BaseModel


class ProjectModel(BaseModel):
    project_name: Optional[str] = None

    def marshal(self, format: str = "json") -> dict:
        """
        marshal the ProjectModel instance and return a dictionary containing
        the ProjectModel instance's attributes

        :return:
        """
        print(self)
        ret = {
            "project_name": self.project_name
        }

        if format == "cloudevent":
            return {k.replace("_", ""): v for k, v in ret.items()}
        else:
            return ret

    @classmethod
    def unmarshal(cls, data: dict):
        """
        Unmarshal the ProjectModel instance and return a new instance of ProjectModel
        from a dictionary containing a ProjectModel instance's attributes

        :param data:
        """

        return ProjectModel(
            project_name=data.get("project_name", "projectname")
        )
