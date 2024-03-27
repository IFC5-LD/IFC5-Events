from typing import Optional

from pydantic import BaseModel

from resources.models.author import AuthorModel
from resources.models.data import DataModel
from resources.models.project import ProjectModel
from resources.models.schema import SchemaModel


class EventModel(BaseModel):
    entity_id: str = None
    component_id: str = None
    _schema: Optional[SchemaModel] = None
    _project: Optional[ProjectModel] = None
    _author: Optional[AuthorModel] = None
    _data: Optional[DataModel] = None

    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, value: SchemaModel) -> None:
        self._schema = value

    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, value: ProjectModel) -> None:
        self._project = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value: AuthorModel) -> None:
        self._author = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value: DataModel) -> None:
        self._data = value

