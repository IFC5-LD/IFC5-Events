import json
import os

from resources.models.schema import SchemaModel
from jsonschema import validate
from jsonschema.validators import Draft202012Validator
import aiohttp
import aiofiles
import asyncio


class Schema:
    _schema: dict
    _model: SchemaModel

    def __init__(self, schema_name: str, schema_uri: str):
        self._model.schemaname = schema_name
        self._model.schemauri = schema_uri

    async def retrieve(self, uri: str = None) -> None:
        """
        Name: retrieve
        Signature: retrieve(self)
        Return: dict
        Description: This method is used to retrieve the schema from the schema uri

        Example:
            schema = Schema("example", "https://example.com/event.schema.json")
            json_schema = schema.retrieve()
        """

        if uri:
            self._model.schemauri = uri

        if os.getenv("IFC_ENV", "dev") == "dev":
            async with aiofiles.open(self._model.schemauri, mode='r') as file:
                self._schema = json.loads(await file.read())
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(self._model.schemauri) as response:
                    self._schema = await response.json()

    def json_schema(self) -> dict:
        return self._schema

    def marshal(self) -> dict:
        self._model.marshal().update(self._schema)
        return self._model.marshal()

    def unmarshal(self, data: dict) -> None:
        self._model.unmarshal(data)
        self._schema = self.retrieve()

    def validate(self, instance: dict) -> bool:
        return validate(instance, self._schema, validator=Draft202012Validator)
