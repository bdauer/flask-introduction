import sqlite3
from contextlib import closing

import click

from library import config


@click.group()
def cli():
    pass


def get_connection():
    return sqlite3.connect(config.DATABASE_NAME)


@cli.command()
def init_db():
    with closing(get_connection()) as db:
        with open('library-schema.sql', 'r') as f_schema, \
             open('initial-data.sql', 'r') as f_data:
            db.executescript(f_schema.read())
            db.executescript(f_data.read())
        db.commit()


@cli.command()
def add_author(name, country_id):
    with closing(get_connection()) as db:
        cursor = db.cursor()
        cursor.execute(
            'INSERT INTO author (name, country_id) VALUES ("{}", "{}")'.format(
                name, country_id))
        db.commit()


@cli.command()
def print_authors():
    with closing(get_connection()) as db:
        cursor = db.execute('SELECT id, name FROM author;')
        authors = cursor.fetchall()
        print("Authors (id - name): ")
        for author in authors:
            print("{} - {}".format(author[0], author[1]))


BOOK_QUERY = """SELECT b.id, b.title, a.name name FROM
                book b INNER JOIN author a ON (b.author_id = a.id);"""


@cli.command()
@cli.argument()
def add_book(name, title, author_id, isbn=None):
    with closing(get_connection()) as db:
        cursor = db.cursor()
        cursor.execute(
            'INSERT INTO book (title, author_id) '
            'VALUES ("{}", "{}", "{}")'.format(
                name, author_id, isbn))
        db.commit()


@cli.command()
def print_books():
    with closing(get_connection()) as db:
        cursor = db.execute(BOOK_QUERY)
        books = cursor.fetchall()
        click.echo(" Books(id - title - author): \n")
        for book in books:
            print("{} - {} - {}".format(*book))


if __name__ == '__main__':
    cli()
