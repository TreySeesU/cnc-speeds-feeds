"""
CNC Speeds & Feeds Manager
Database Management Module

Handles all SQLite database connections,
queries, transactions, and common CRUD operations.

Python Version:
3.12+

Author:
TreySeesU
"""


import sqlite3
from pathlib import Path
from typing import Any, Optional

from config import DATABASE_FILE, DATABASE_TIMEOUT


# ==========================================================
# DATABASE CONNECTION
# ==========================================================

def get_connection() -> sqlite3.Connection:
    """
    Creates and returns a SQLite database connection.

    Foreign key enforcement is enabled automatically.
    """

    connection = sqlite3.connect(
        DATABASE_FILE,
        timeout=DATABASE_TIMEOUT
    )


    connection.row_factory = sqlite3.Row


    connection.execute(
        "PRAGMA foreign_keys = ON;"
    )


    return connection



# ==========================================================
# QUERY FUNCTIONS
# ==========================================================

def execute_query(
    query: str,
    parameters: tuple = ()
) -> list:

    """
    Executes a SELECT query and returns rows.

    Example:

        materials = execute_query(
            "SELECT * FROM materials"
        )
    """

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            query,
            parameters
        )

        results = cursor.fetchall()

        return results


    finally:

        connection.close()



def execute_one(
    query: str,
    parameters: tuple = ()
) -> Optional[sqlite3.Row]:

    """
    Executes a SELECT query and returns
    a single record.
    """

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            query,
            parameters
        )

        return cursor.fetchone()


    finally:

        connection.close()



# ==========================================================
# INSERT / UPDATE / DELETE
# ==========================================================

def execute_action(
    query: str,
    parameters: tuple = ()
) -> int:

    """
    Executes INSERT, UPDATE, or DELETE.

    Returns:
        Last inserted row ID.
    """

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            query,
            parameters
        )

        connection.commit()

        return cursor.lastrowid


    except Exception:

        connection.rollback()

        raise


    finally:

        connection.close()



# ==========================================================
# TRANSACTION SUPPORT
# ==========================================================

def execute_transaction(
    commands: list
):

    """
    Executes multiple database commands
    inside one transaction.

    commands format:

    [
        (
            "SQL QUERY",
            (parameters,)
        )
    ]

    """

    connection = get_connection()


    try:

        cursor = connection.cursor()


        for command, parameters in commands:

            cursor.execute(
                command,
                parameters
            )


        connection.commit()


    except Exception:

        connection.rollback()

        raise


    finally:

        connection.close()



# ==========================================================
# DATABASE TEST
# ==========================================================

def test_connection() -> bool:

    """
    Tests database connectivity.
    """

    try:

        connection = get_connection()

        connection.close()

        return True


    except sqlite3.Error:

        return False



# ==========================================================
# MATERIAL FUNCTIONS
# ==========================================================

def get_materials():

    """
    Returns all materials.
    """

    return execute_query(
        """
        SELECT *
        FROM materials
        ORDER BY name
        """
    )



def get_material(
    material_id: int
):

    """
    Returns one material by ID.
    """

    return execute_one(
        """
        SELECT *
        FROM materials
        WHERE id = ?
        """,
        (material_id,)
    )



# ==========================================================
# TOOL FUNCTIONS
# ==========================================================

def get_tools():

    """
    Returns all tools.
    """

    return execute_query(
        """
        SELECT
            tools.*,
            tool_types.name AS tool_type

        FROM tools

        LEFT JOIN tool_types

        ON tools.tool_type_id =
           tool_types.id

        ORDER BY tools.name

        """
    )



def get_tool(
    tool_id: int
):

    """
    Returns a single tool.
    """

    return execute_one(
        """
        SELECT *
        FROM tools
        WHERE id = ?
        """,
        (tool_id,)
    )



# ==========================================================
# MACHINE FUNCTIONS
# ==========================================================

def get_machines():

    """
    Returns all machines.
    """

    return execute_query(
        """
        SELECT *
        FROM machines
        ORDER BY name
        """
    )



def get_machine(
    machine_id: int
):

    """
    Returns one machine.
    """

    return execute_one(
        """
        SELECT *
        FROM machines
        WHERE id = ?
        """,
        (machine_id,)
    )



# ==========================================================
# LOOKUP FUNCTIONS
# ==========================================================

def get_tool_types():

    return execute_query(
        """
        SELECT *
        FROM tool_types
        ORDER BY name
        """
    )



def get_material_categories():

    return execute_query(
        """
        SELECT *
        FROM material_categories
        ORDER BY name
        """
    )



def get_cut_directions():

    return execute_query(
        """
        SELECT *
        FROM cut_directions
        ORDER BY name
        """
    )



def get_units():

    return execute_query(
        """
        SELECT *
        FROM units
        ORDER BY name
        """
    )



# ==========================================================
# DATABASE HEALTH CHECK
# ==========================================================

def database_status():

    """
    Returns basic database information.
    """

    status = {

        "database":
            str(DATABASE_FILE),

        "connected":
            test_connection()

    }


    return status



# ==========================================================
# COMMAND LINE TEST
# ==========================================================

if __name__ == "__main__":


    print(
        "Database Status:"
    )


    print(
        database_status()
    )


    print()


    print(
        "Materials:"
    )


    for material in get_materials():

        print(
            dict(material)
        )
