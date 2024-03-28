import asyncio
import json
import logging
import uuid

import click
import dotenv

from resources import IFCEvent, Schema
from resources.models import DataModel, AuthorModel, SchemaModel, ProjectModel


@click.command("create-event")
@click.option("--instance", "-i", help="The path to the instance of the event data", required=False)
@click.option("--schema", "-sc", help="The path to the schema of the event", required=False)
@click.option("--test", is_flag=True, help="Run the test suite", default=False)
def create_event(
        instance: str,
        schema: str,
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
            data=json.load(open("data/instances/tests/author.json"))
        )
        event.model.schema = SchemaModel.unmarshal(
            data=json.load(open("data/instances/tests/schema.json"))
        )

        event.model.project = ProjectModel.unmarshal(
            data=json.load(open("data/instances/tests/project.json"))
        )

        event.model.data = DataModel.unmarshal(
            data=json.load(open("data/instances/tests/data.json"))
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
