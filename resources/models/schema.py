from typing import Union
from pydantic import BaseModel

from resources.models.helpers.hash import hash


class SchemaModel(BaseModel):
    schema_name: str
    schema_uri: str
    schema_version: str
    schema_hash: str

    @property
    def schemaname(self):
        return self.schema_name

    @schemaname.setter
    def schemaname(self, value: str) -> None:
        self.schema_name = value

    @schemaname.deleter
    def schemaname(self) -> str:
        tmp = self.schema_name
        self.schema_name = None

        return tmp

    @property
    def schemauri(self):
        return self.schema_uri

    @schemauri.setter
    def schemauri(self, value: str) -> None:
        self.schema_uri = value

    @schemauri.deleter
    def schemauri(self) -> str:
        tmp = self.schema_uri
        self.schema_uri = None

        return tmp

    @property
    def schemaversion(self):
        return self.schema_version

    @schemaversion.setter
    def schemaversion(self, value: str) -> None:
        self.schema_version = value

    @schemaversion.deleter
    def schemaversion(self) -> str:
        Warning("Deleting the schema version is not allowed")

    @property
    def schemahash(self):
        return self.schema_hash

    @schemahash.setter
    def schemahash(self, value: str, schema: Union[str, dict] = None) -> None:
        if schema:
            self.schema_hash = hash(schema)
        else:
            self.schema_hash = value

    @schemahash.deleter
    def schemahash(self) -> None:
        Warning("Deleting the schema hash is not allowed")

    def marshal(self, format: str = "json") -> dict:
        """
        marshal the SchemaModel instance and return a dictionary containing the SchemaModel instance's attributes
        in CloudEvent format
        :return:
        """
        ret = {
            "schema_name": self.schemaname,
            "schema_uri": self.schemauri,
            "schema_version": self.schemaversion,
            "schema_hash": self.schemahash
        }

        if format == "cloudevent":
            return {k.replace("_", ""): v for k, v in ret.items()}
        else:
            return ret

    @classmethod
    def unmarshal(cls, data: dict):

        return SchemaModel(
            schema_name=data.get("schema_name", "schemaname"),
            schema_uri=data.get("schema_uri", "schemauri"),
            schema_version=data.get("schema_version", "schemaversion"),
            schema_hash=data.get("schema_hash", hash(data.get("schema", {})))
        )