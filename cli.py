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
@click.option("--entityid", "-e", help="The entity ID of the event", required=False, default=str(uuid.uuid4()))
@click.option("--componentid", "-c", help="The component ID of the event", required=False, default=str(uuid.uuid4()))
@click.option("--instance", "-i", help="The instance of the event", required=False, default={})
@click.option("--schema", "-sc", help="The schema of the event", required=False, default={})
@click.option("--test", is_flag=True, help="Run the test suite", default=False)
def create_event(
        source: str,
        type: str,
        entityid: str,
        componentid: str,
        instance: dict,
        schema: dict,
        test: bool
):
    event = IFCEvent(
        source="https://example.com",
        type="com.example.event",
        entityid="123e4567-e89b-12d3-a456-426614174000",
        componentid="123e4567-e89b-12d3-a456-426614174000",
    )

    if test:

        event.model.author.unmarshal(
            data={
                "authorname": "John Doe",
                "authorid": "123e4567-e89b-12d3-a456-426614174000",
                "authortoken": "123e4567-e89b-12d3-a456-426614174000"
            }
        )
        event.model.schema.unmarshal(
            data={
                "_schema_name": "example",
                "_schema_uri": "data/schema/event.schema.json",
                "_schema_version": "1.0.0",
                "_schema_hash": "123e4567-e89b-12d3-a456-426614174000"
            }
        )

        event.model.project.unmarshal(
            data={
                "project_name": "example",
                "project_id": "123e4567-e89b-12d3-a456-426614174000"
            }
        )
        data = json.load(open("data/instances/example.json"))

        event.model.data.unmarshal(
            data={
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
    click.echo(f'Event ID: {event.entityid}')
    click.echo(f"Payload: {event.marshal()}")


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
