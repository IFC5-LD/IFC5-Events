import asyncio
import json
import logging
import uuid

import click
import dotenv

from resources import IFCEvent, Schema
from resources.models import DataModel, AuthorModel, SchemaModel, ProjectModel

@click.command("create-event")
@click.option("--source", "-s", help="The source of the event", required=False, default="https://example.com")
@click.option("--type", "-t", help="The type of the event", required=False, default="com.example.event")
@click.option("--entity-id", "-e", "entity_id", help="The entity ID of the event", required=False, default=str(uuid.uuid4()))
@click.option("--component-id", "-c", "component_id", help="The component ID of the event", required=False, default=str(uuid.uuid4()))
@click.option("--instance", "-i", help="The instance of the event", required=False, default={})
@click.option("--schema", "-sc", help="The schema of the event", required=False, default={})
@click.option("--test", is_flag=True, help="Run the test suite", default=False)
def create_event(
        source: str,
        type: str,
        entity_id: str,
        component_id: str,
        instance: dict,
        schema: dict,
        test: bool
):
    event = IFCEvent(
        source="https://example.com",
        type="com.example.event",
        entity_id="123e4567-e89b-12d3-a456-426614174000",
        component_id="123e4567-e89b-12d3-a456-426614174000",
    )

    if test:

        event.model.author = AuthorModel.unmarshal(
            data={
                "author_name": "John Doe",
                "author_id": "123e4567-e89b-12d3-a456-426614174000",
                "author_token": "123e4567-e89b-12d3-a456-426614174000"
            }
        )
        event.model.schema = SchemaModel.unmarshal(
            data={
                "schema_name": "example",
                "schema_uri": "data/schema/event.schema.json",
                "schema_version": "1.0.0",
                "schema_hash": "123e4567-e89b-12d3-a456-426614174000"
            }
        )

        event.model.project = ProjectModel.unmarshal(
            data={
                "project_name": "example",
                "project_id": "123e4567-e89b-12d3-a456-426614174000"
            }
        )
        data = json.load(open("data/instances/example.json"))

        event.model.data = DataModel.unmarshal(
            data={
                "data_encoding": "utf-8",
                "data_encryption": "test",
                "data": {"key": "value"}
            }
        )
    else:
        event.model.author = AuthorModel(data={"name": "John Doe", "email": "test@example.com"})
        event.model.schema = SchemaModel(data={
            "$schema": "http://json-schema.org/draft-07/schema#",
            "title": "example",
            "type": "object",
            "properties": {"key": {"type": "string"}}
        })
        event.model.project = ProjectModel(data={"name": "example"})
        event.model.data = DataModel(data={"key": "value"})
    click.echo('Creating a new event...')
    click.echo(f'Event ID: {event.entity_id}')
    click.echo(f"Payload: {event.marshal().json()}")


@click.command("get-schema")
def get_schema():
    click.echo('Getting schema...')


@click.group("ifc-events")
def cli():
    dotenv.load_dotenv(".env")
    click.echo('Hello, World!')


cli.add_command(create_event)
cli.add_command(get_schema)

if __name__ == '__main__':
    cli()
