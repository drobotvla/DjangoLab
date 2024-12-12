from django.db import models


class Supplier(models.Model):
    company_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    payment_account = models.CharField(max_length=30)


class Material(models.Model):
    material_code = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Supply(models.Model):
    supply_id = models.AutoField(primary_key=True)
    supply_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    time_consumption = models.IntegerField()
    amount = models.IntegerField()
