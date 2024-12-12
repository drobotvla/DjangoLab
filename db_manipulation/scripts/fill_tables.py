#!/usr/bin/env python

import random
import datetime

from db import get_cursor

with get_cursor() as cursor:
    suppliers = [
        ("Supplier A", "John Doe", "+123-456-7890", "ACCT123"),
        ("Supplier B", "Jane Smith", "+987-654-3210", "ACCT456"),
        ("Supplier C", "Michael Johnson", "+555-555-5555", "ACCT789"),
        ("Supplier D", "Emily Davis", "+111-222-3333", "ACCT012")
    ]

    materials = [
        ("WOOD", "Wood", 10.00),
        ("VARNISH", "Varnish", 5.00),
        ("STEEL_DETAILS", "Steel Details", 20.00)
    ]

    insert_supplier_query = """
        INSERT INTO Suppliers (company_name, contact_person, phone_number, payment_account)
        VALUES (%s, %s, %s, %s)
    """
    cursor.executemany(insert_supplier_query, suppliers)

    insert_material_query = """
        INSERT INTO Materials (material_code, name, price)
        VALUES (%s, %s, %s)
    """
    cursor.executemany(insert_material_query, materials)

    supply_data = []
    for _ in range(22):
        supplier_id = random.randint(1, 4)
        material_code = random.choice(["WOOD", "VARNISH", "STEEL_DETAILS"])
        time_consumption = random.randint(1, 7)
        amount = random.randint(10, 100)
        supply_date = datetime.date(2023, random.randint(1, 12), random.randint(1, 28))
        supply_data.append((supply_date, supplier_id, material_code, time_consumption, amount))

    insert_supply_query = """
        INSERT INTO Supplies (supply_date, supplier_code, material_code, time_consumption, amount)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.executemany(insert_supply_query, supply_data)

    print("Data inserted successfully!")
