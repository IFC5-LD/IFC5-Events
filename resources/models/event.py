from pydantic import BaseModel

from resources.models.author import AuthorModel
from resources.models.data import DataModel
from resources.models.project import ProjectModel
from resources.models.schema import SchemaModel

class EventModel(BaseModel):
    _entityid: str
    _componentid: str
    _schema: SchemaModel
    _author: AuthorModel
    _data: DataModel
    _project: ProjectModel

    @property
    def entityid(self):
        return self._entityid

    @entityid.setter
    def entityid(self, value: str) -> None:
        self._entityid = value

    @property
    def componentid(self):
        return self._componentid

    @componentid.setter
    def componentid(self, value: str) -> None:
        self._componentid = value

    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, value: SchemaModel) -> None:
        self._schema = value

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

    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, value: ProjectModel) -> None:
        self._project = value
