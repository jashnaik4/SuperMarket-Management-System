# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customers(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    address = models.TextField()
    contact_information = models.BigIntegerField()


class Employees(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    address = models.TextField()
    contact_information = models.BigIntegerField()
    job_position = models.CharField(max_length=255)


class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()


class PurchaseItems(models.Model):
    purchase = models.ForeignKey('Purchases', models.DO_NOTHING)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    quantity_purchased = models.IntegerField()


class Purchases(models.Model):
    purchase_id = models.IntegerField(primary_key=True)
    purchase_date = models.DateField()
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING)


class SaleItems(models.Model):
    sale = models.ForeignKey('Sales', models.DO_NOTHING)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    quantity_sold = models.IntegerField()


class Sales(models.Model):
    sale_id = models.IntegerField(primary_key=True)
    sale_date = models.DateField()
    customer = models.ForeignKey(Customers, models.DO_NOTHING)
    employee = models.ForeignKey(Employees, models.DO_NOTHING, blank=True, null=True)


class Suppliers(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    supplier_name = models.CharField(max_length=255)
    address = models.TextField()
    contact_information = models.BigIntegerField()


class SaleRecord(models.Model):
    sale_id = models.ForeignKey(Sales, models.DO_NOTHING)
    customer_name = models.CharField(max_length=255)
    employee_name = models.CharField(max_length=255)
    sale_date = models.DateField()
    product_name = models.CharField(max_length=255)
    quantity_sold = models.IntegerField()


class PurchaseRecord(models.Model):
    purchase_id = models.ForeignKey(Purchases, models.DO_NOTHING)
    product_name = models.CharField(max_length=255)
    supplier_name = models.CharField(max_length=255)
    purchase_date = models.DateField()
    quantity_purchased = models.IntegerField()


class InventoryReport(models.Model):
    product_id = models.ForeignKey(Products, models.DO_NOTHING)
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity_in_stock = models.IntegerField()
    quantity_sold = models.IntegerField()
    revenue = models.IntegerField()



