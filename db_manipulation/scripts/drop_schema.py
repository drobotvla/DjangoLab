#!/usr/bin/env python

import psycopg2

from db import get_cursor

DROP_SUPPLIERS_TABLE = """
    DROP TABLE Suppliers
"""

DROP_MATERIALS_TABLE = """
    DROP TABLE Materials
"""

DROP_SUPPLIES_TABLE = """
    DROP TABLE Supplies
"""

DROP_TABLES = [
    DROP_SUPPLIERS_TABLE,
    DROP_MATERIALS_TABLE,
    DROP_SUPPLIES_TABLE
]

with get_cursor() as cursor:
    for drop_request in DROP_TABLES:
        cursor.execute(drop_request)

    print("Tables dropped successfully!")
