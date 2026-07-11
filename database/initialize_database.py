```python
"""
CNC Speeds & Feeds Manager
Database Initialization Script

Creates the SQLite database and initializes required lookup tables.

Python Version:
3.12+

Database:
SQLite 3

Author:
TreySeesU
"""

import sqlite3
import os
from pathlib import Path


# ==========================================================
# PATH CONFIGURATION
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

DATABASE_FILE = BASE_DIR / "cnc.db"

SCHEMA_FILE = BASE_DIR / "schema.sql"


# ==========================================================
# INITIAL LOOKUP DATA
# ==========================================================

UNITS = [
    ("Millimeter",),
    ("Inch",),
    ("mm/min",),
    ("in/min",)
]


TOOL_TYPES = [
    (
        "Straight Flute",
        "Straight cutting edge router bit"
    ),
    (
        "Spiral Upcut",
        "Helical flute tool with upward chip evacuation"
    ),
    (
        "Spiral Downcut",
        "Helical flute tool with downward chip evacuation"
    ),
    (
        "Compression",
        "Combination upcut and downcut geometry"
    ),
    (
        "O-Flute",
        "Single or double flute plastic cutting tool"
    ),
    (
        "Ball Nose",
        "Rounded cutting tool for 3D machining"
    ),
    (
        "Tapered Ball Nose",
        "Tapered tool for detailed 3D carving"
    ),
    (
        "V-Bit",
        "Engraving and chamfer tool"
    ),
    (
        "Surfacing",
        "Spoilboard surfacing cutter"
    ),
    (
        "Roughing End Mill",
        "High material removal tool"
    ),
    (
        "Finishing End Mill",
        "Finishing cutter"
    )
]


CUT_DIRECTIONS = [
    ("Climb",),
    ("Conventional",)
]


MATERIAL_CATEGORIES = [
    ("Wood",),
    ("Plastic",),
    ("Composite",),
    ("Metal",),
    ("Foam",),
    ("Other",)
]


DEFAULT_SETTINGS = [
    (
        "default_units",
        "metric"
    ),
    (
        "default_feed_units",
        "mm/min"
    ),
    (
        "application_version",
        "1.0.0"
    )
]


# ==========================================================
# CREATE DATABASE
# ==========================================================

def create_database():

    if not SCHEMA_FILE.exists():

        raise FileNotFoundError(
            f"Schema file not found: {SCHEMA_FILE}"
        )


    print("Creating database...")


    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()


    with open(
        SCHEMA_FILE,
        "r",
        encoding="utf-8"
    ) as schema_file:

        schema = schema_file.read()

        cursor.executescript(schema)


    connection.commit()

    connection.close()


    print(
        f"Database created: {DATABASE_FILE}"
    )


# ==========================================================
# INSERT LOOKUP DATA
# ==========================================================

def insert_lookup_data():

    print("Adding lookup data...")


    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()


    cursor.executemany(
        """
        INSERT INTO units(name)
        VALUES (?)
        """,
        UNITS
    )


    cursor.executemany(
        """
        INSERT INTO tool_types
        (
            name,
            description
        )
        VALUES (?,?)
        """,
        TOOL_TYPES
    )


    cursor.executemany(
        """
        INSERT INTO cut_directions(name)
        VALUES (?)
        """,
        CUT_DIRECTIONS
    )


    cursor.executemany(
        """
        INSERT INTO material_categories(name)
        VALUES (?)
        """,
        MATERIAL_CATEGORIES
    )


    cursor.executemany(
        """
        INSERT INTO settings
        (
            setting_name,
            setting_value
        )
        VALUES (?,?)
        """,
        DEFAULT_SETTINGS
    )


    cursor.execute(
        """
        INSERT INTO database_info(version)
        VALUES ('1.0.0')
        """
    )


    connection.commit()

    connection.close()


    print("Lookup data added.")


# ==========================================================
# MAIN
# ==========================================================

def main():

    if DATABASE_FILE.exists():

        print(
            "Database already exists:"
        )

        print(
            DATABASE_FILE
        )

        response = input(
            "Overwrite existing database? (yes/no): "
        )


        if response.lower() != "yes":

            print(
                "Database creation cancelled."
            )

            return


        os.remove(DATABASE_FILE)


    create_database()

    insert_lookup_data()


    print()
    print(
        "CNC Speeds & Feeds database initialization complete."
    )


if __name__ == "__main__":

    main()
```
