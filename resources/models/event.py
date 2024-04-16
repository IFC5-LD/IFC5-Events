from typing import Optional

from pydantic import BaseModel

from resources.models.author import AuthorModel
from resources.models.data import DataModel
from resources.models.project import ProjectModel
from resources.models.schema import SchemaModel


class EventModel(BaseModel):
    entity_id: str = None
    component_id: str = None
    schema: Optional[SchemaModel] = None
    project: Optional[ProjectModel] = None
    author: Optional[AuthorModel] = None
    data: Optional[DataModel] = None

