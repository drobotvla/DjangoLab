from django.shortcuts import render

from .models import Supplier, Material, Supply

def index(request):
    suppliers = Supplier.objects.all()
    materials = Material.objects.all()
    supplies = Supply.objects.all()

    tables = {
        "Suppliers": [
            ["Company name", "Contact person", "Phone number", "Payment Account"],
            [
                [
                    supplier.company_name,
                    supplier.contact_person,
                    supplier.phone_number,
                    supplier.payment_account
                ] for supplier in suppliers
            ]
        ],
        "Materials": [
            ["Material Code", "Name", "Price"],
            [
                [
                    material.material_code, material.name, material.price
                ]
                for material in materials
            ]
        ],
        "Supplies": [
            ["Supply Date", "Supplier", "Material", "Time Consumption(days)", "Amount"],
            [
                [
                    supply.supply_date,
                    supply.supplier.company_name,
                    supply.material.name,
                    supply.time_consumption,
                    supply.amount
                ]
                for supply in supplies
            ]
        ],
    }

    context = {
        "tables": tables
    }

    return render(request, "index.html", context)
