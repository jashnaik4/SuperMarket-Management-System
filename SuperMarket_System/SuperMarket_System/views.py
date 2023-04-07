from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        sql_query = "INSERT INTO customers VALUES(" + request.POST["c_id"] +", '" + request.POST["name"] + "', '" +request.POST["address"] + "', " + request.POST["number"]+")"
        try :
            cursor.execute(sql_query)
        except :
            print("ERROR : SQL Query -> " + sql_query)
    cursor.execute("SELECT * FROM customers")
    results = cursor.fetchall()
    return render(request, 'customers.html', {'Customers': results})

def deleteCustomer(request,customer_id):
    cursor = connection.cursor()
    sql_query = "DELETE FROM customers WHERE customer_id = " + str(customer_id)
    cursor.execute(sql_query)
    return redirect("/customers/")

def updateCustomer(request,customer_id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customers WHERE customer_id = " + str(customer_id))
    customer = cursor.fetchone()
    return render(request, 'customers_update.html', {"Customers": customer})

def commitUpdate(request, id):
    cursor = connection.cursor()
    if request.method == 'POST':
        sql_query = "UPDATE customers SET customer_name = '" + request.POST["name"] + "', address =  '" +request.POST["address"] + "', contact_information = " + request.POST["number"] + " WHERE customer_id = " + str(id)
        try :
            cursor.execute(sql_query)
        except :
            print("ERROR : SQL Query -> " + sql_query)

    return redirect("/customers/")