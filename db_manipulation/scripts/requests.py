#!/usr/bin/env python

from tabulate import tabulate
from db import get_cursor


with get_cursor() as cursor:
    #1
    cursor.execute("""
        SELECT s.company_name, sp.supply_date
        FROM Supplies sp
        JOIN Suppliers s ON sp.supplier_code = s.id
        WHERE sp.supply_date BETWEEN CURRENT_DATE - INTERVAL '3 DAY' AND CURRENT_DATE
        ORDER BY s.company_name;
    """
    )

    supplies_last_3_days = cursor.fetchall()
    print("Supplies within the Last 3 Days (Sorted by Supplier Name):")
    print(tabulate(supplies_last_3_days, headers=["Supplier Name", "Supply Date"], tablefmt="grid"))


    #2
    cursor.execute("""
        SELECT sp.supply_id, SUM(m.price * sp.amount) AS total_cost
        FROM Supplies sp
        JOIN Materials m ON sp.material_code = m.material_code
        GROUP BY sp.supply_id;
    """
    )

    total_cost_per_supply = cursor.fetchall()
    print("\nTotal Cost per Supply:")
    print(tabulate(total_cost_per_supply, headers=["Supply ID", "Total Cost"], tablefmt="grid"))

    #3
    material_name = "Varnish"

    cursor.execute("""
        SELECT s.company_name, sp.supply_date, m.name, sp.amount
        FROM Supplies sp
        JOIN Suppliers s ON sp.supplier_code = s.id
        JOIN Materials m ON sp.material_code = m.material_code
        WHERE m.name = %s;
    """, (material_name, )
    )

    supplies_with_material = cursor.fetchall()
    print(f"\nSupplies with Material: {material_name}")
    print(tabulate(supplies_with_material, headers=["Supplier Name", "Supply Date", "Material", "Amount"], tablefmt="grid"))

    #4
    cursor.execute("""
        SELECT s.company_name, m.name, SUM(sp.amount) AS total_amount
        FROM Supplies sp
        JOIN Suppliers s ON sp.supplier_code = s.id
        JOIN Materials m ON sp.material_code = m.material_code
        GROUP BY s.company_name, m.name;
    """
    )

    material_by_supplier = cursor.fetchall()
    print("\nAmount of Each Material Supplied by Each Supplier:")
    print(tabulate(material_by_supplier, headers=["Supplier Name", "Material", "Total Amount"], tablefmt="grid"))

    #5
    cursor.execute("""
        SELECT m.name, SUM(sp.amount) AS total_amount
        FROM Supplies sp
        JOIN Materials m ON sp.material_code = m.material_code
        GROUP BY m.name;
    """)

    total_material_amount = cursor.fetchall()
    print("\nGeneral Amount of Each Material:")
    print(tabulate(total_material_amount, headers=["Material", "Total Amount"], tablefmt="grid"))

    #6
    cursor.execute("""
        SELECT s.company_name, COUNT(*) AS total_supplies
        FROM Supplies sp
        JOIN Suppliers s ON sp.supplier_code = s.id
        GROUP BY s.company_name;
    """)

    supplier_supply_count = cursor.fetchall()
    print("\nAmount of Supplies for Each Supplier:")
    print(tabulate(supplier_supply_count, headers=["Supplier Name", "Total Supplies"], tablefmt="grid"))
