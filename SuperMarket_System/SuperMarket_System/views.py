from django.shortcuts import render
from django.db import connection

from SuperMarket_System.models import Products
from SuperMarket_System.models import Customers

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def showProducts(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()
    return render(request, 'index.html', {'Products': results})

def showCustomers(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customers")
    results = cursor.fetchall()
    return render(request, 'customers.html', {'Customers': results})

def showEmployees(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    results = cursor.fetchall()
    return render(request, 'employees.html', {'Employees': results})
