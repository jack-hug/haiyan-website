import click
from . import app,db
from .models import Message


@app.cli.command()
@click.option('--count', default = 20, help = 'Quantity of messages, default is 20...')
def forge(count):
    """Generate fake messages"""
    from faker import Faker
    db.drop_all()
    db.create_all()

    faker = Faker()
    click.echo('Working...')

    for i in range(count):
        message = Message(
            name = faker.name(),
            body = faker.sentence(),
            email = faker.email(),
            timestamp = faker.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    click.echo('Create %d fake messages...' % count)