import os
from pathlib import Path

from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine, text

DEFAULT_DB = Path(__file__).resolve().parents[1] / "data" / "demo.db"
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DEFAULT_DB.as_posix()}")


def get_engine():
    return create_engine(DATABASE_URL)


def get_sql_database() -> SQLDatabase:
    return SQLDatabase(get_engine())


def initialize_database() -> None:
    engine = get_engine()
    with engine.begin() as connection:
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """))
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                department_id INTEGER NOT NULL,
                salary INTEGER NOT NULL,
                FOREIGN KEY (department_id) REFERENCES departments(id)
            )
        """))
        count = connection.execute(text("SELECT COUNT(*) FROM employees")).scalar_one()
        if count == 0:
            connection.execute(
                text("INSERT INTO departments (id, name) VALUES "
                     "(1, 'Engineering'), (2, 'Finance'), (3, 'Operations')")
            )
            connection.execute(
                text("INSERT INTO employees (id, name, department_id, salary) VALUES "
                     "(1, 'Alex', 1, 92000), (2, 'Sam', 1, 88000), "
                     "(3, 'Jordan', 2, 79000), (4, 'Taylor', 2, 83000), "
                     "(5, 'Morgan', 3, 68000)")
            )
