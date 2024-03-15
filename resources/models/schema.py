from typing import Union
from pydantic import BaseModel

from resources.models.helpers.hash import hash

class SchemaModel(BaseModel):
    _schema_name: str
    _schema_uri: str
    _schema_version: str
    _schema_hash: str

    @property
    def schemaname(self):
        return self._schema_name

    @schemaname.setter
    def schemaname(self, value: str) -> None:
        self._schema_name = value

    @schemaname.deleter
    def schemaname(self) -> str:
        tmp = self._schema_name
        self._schema_name = None

        return tmp

    @property
    def schemauri(self):
        return self._schema_uri

    @schemauri.setter
    def schemauri(self, value: str) -> None:
        self._schema_uri = value

    @schemauri.deleter
    def schemauri(self) -> str:
        tmp = self._schema_uri
        self._schema_uri = None

        return tmp

    @property
    def schemaversion(self):
        return self._schema_version

    @schemaversion.setter
    def schemaversion(self, value: str) -> None:
        self._schema_version = value

    @schemaversion.deleter
    def schemaversion(self) -> str:
        Warning("Deleting the schema version is not allowed")

    @property
    def schemahash(self):
        return self._schema_hash

    @schemahash.setter
    def schemahash(self, value: str, schema: Union[str, dict]=None) -> None:
        if schema:
            self._schema_hash = hash(schema)
        else:
            self._schema_hash = value

    @schemahash.deleter
    def schemahash(self) -> None:
        Warning("Deleting the schema hash is not allowed")

    def marshal(self) -> dict:
        return self.dict()

    def unmarshal(self, data: dict) -> None:
        self._schema_name = data['_schema_name']
        self._schema_uri = data['_schema_uri']
        self._schema_version = data['_schema_version']
        self._schema_hash = data['_schema_hash']
