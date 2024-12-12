#!/usr/bin/env python

import psycopg2

from db import get_cursor

CREATE_SUPPLIERS_TABLE = """
    CREATE TABLE Suppliers (
        id SERIAL PRIMARY KEY,
        company_name VARCHAR(100) NOT NULL,
        contact_person VARCHAR(50),
        phone_number VARCHAR(20),
        payment_account VARCHAR(30)
    );
"""

CREATE_MATERIALS_TABLE = """
    CREATE TABLE Materials (
        material_code VARCHAR(20) PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price DECIMAL(10, 2)
    );
"""

CREATE_SUPPLIES_TABLE = """
    CREATE TABLE Supplies (
        supply_id SERIAL PRIMARY KEY,
        supply_date DATE,
        supplier_code INTEGER REFERENCES Suppliers(id),
        material_code VARCHAR(20) REFERENCES Materials(material_code),
        time_consumption INT CHECK (time_consumption BETWEEN 1 AND 7),
        amount INT
    );
"""

CREATE_TABLES = [
    CREATE_SUPPLIERS_TABLE,
    CREATE_MATERIALS_TABLE,
    CREATE_SUPPLIES_TABLE
]

with get_cursor() as cursor:
    for create_request in CREATE_TABLES:
        cursor.execute(create_request)

    print("Tables created successfully!")
