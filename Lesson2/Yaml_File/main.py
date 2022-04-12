import click
from schema import SchemaFile

@click.group()
def cli():
    pass

@cli.command()
def configure():
    """Simple program that greets NAME for a total of COUNT time."""
    
    schema = SchemaFile()
    output_schema = {}
    for key in SCHEMA.keys():
        value =  click.prompt(f"Whata is the {key}")
        output_schema[key] = value

    schema.set_values(output_schema)

if __name__ == '__main__':
    cli()