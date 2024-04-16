from typing import Union
from pydantic import BaseModel

from resources.models.helpers.hash import hash


class SchemaModel(BaseModel):
    schema_name: str
    schema_uri: str
    schema_version: str
    schema_hash: str

    def marshal(self, format: str = "json") -> dict:
        """
        marshal the SchemaModel instance and return a dictionary containing the SchemaModel instance's attributes
        in CloudEvent format

        :return:
        """
        ret = {
            "schema_name": self.schema_name,
            "schema_uri": self.schema_uri,
            "schema_version": self.schema_version,
            "schema_hash": self.schema_hash
        }

        if format == "cloudevent":
            return {k.replace("_", ""): v for k, v in ret.items()}
        else:
            return ret

    @classmethod
    def unmarshal(cls, data: dict) -> "SchemaModel":

        return SchemaModel(
            schema_name=data.get("schema_name", "schemaname"),
            schema_uri=data.get("schema_uri", "schemauri"),
            schema_version=data.get("schema_version", "schemaversion"),
            schema_hash=data.get("schema_hash", hash(data.get("schema", {})))
        )