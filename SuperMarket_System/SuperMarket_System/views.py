from django.shortcuts import render, redirect
from django.db import connection

# from SuperMarket_System.models import Products
# from SuperMarket_System.models import Customers
# from SuperMarket_System.models import SaleRecord
# from SuperMarket_System.models import InventoryReport
# from SuperMarket_System.models import Employees
#

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
    error = False
    if request.method == 'POST':
        sql_query = "INSERT INTO customers VALUES(" + request.POST["c_id"] +", '" + request.POST["name"] + "', '" +request.POST["address"] + "', " + request.POST["number"]+")"
        try :
            cursor.execute(sql_query)
        except :
            print("ERROR : SQL Query -> " + sql_query)
            error = True
    cursor.execute("SELECT * FROM customers")
    results = cursor.fetchall()
    return render(request, 'customers.html', {'Customers': results, 'ERROR_INPUT': error})


def deleteCustomer(request,customer_id):
    cursor = connection.cursor()
    sql_query = "DELETE FROM customers WHERE customer_id = " + str(customer_id)
    error = False
    try :
        cursor.execute(sql_query)
    except :
        error = True
    cursor.execute("SELECT * FROM customers")
    results = cursor.fetchall()
    return render(request, 'customers.html', {'Customers': results, 'ERROR_DELETE': error})


def updateCustomer(request,customer_id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customers WHERE customer_id = " + str(customer_id))
    customer = cursor.fetchone()
    return render(request, 'customers_update.html', {"Customers": customer})


def commitUpdate(request, id):
    cursor = connection.cursor()
    error = False
    if request.method == 'POST':
        sql_query = "UPDATE customers SET customer_name = '" + request.POST["name"] + "', address =  '" +request.POST["address"] + "', contact_information = " + request.POST["number"] + " WHERE customer_id = " + str(id)
        try :
            cursor.execute(sql_query)
        except :
            print("ERROR : SQL Query -> " + sql_query)
            error = True
    cursor.execute("SELECT * FROM customers")
    results = cursor.fetchall()
    return render(request, 'customers.html', {'Customers': results, 'ERROR_UPDATE': error})


def showEmployees(request):
    cursor = connection.cursor()
    error = False
    if request.method == 'POST':
        sql_query = "INSERT INTO employees VALUES(" + request.POST["employee_id"] + ", '" + request.POST["name"] + "', '" +request.POST["address"] + "', " + request.POST["number"] + ", '" +request.POST["job_position"]+"')"
        try :
            cursor.execute(sql_query)
        except :
            error = True
    cursor.execute("SELECT * FROM employees")
    results = cursor.fetchall()
    return render(request, 'employees.html', {'Employees': results, 'ERROR_INPUT': error})


def updateEmployees(request,employee_id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees WHERE employee_id = " + str(employee_id))
    employee = cursor.fetchone()
    return render(request, 'employees_update.html', {"Employees": employee})


def deleteEmployees(request,employee_id):
    cursor = connection.cursor()
    sql_query = "DELETE FROM employees WHERE employee_id = " + str(employee_id)
    error = False
    try :
        cursor.execute(sql_query)
    except:
        error = True
    cursor.execute("SELECT * FROM employees")
    results = cursor.fetchall()
    return render(request, 'employees.html', {'Employees': results, 'ERROR_DELETE': error})


def commitEmpUpdate(request, id):
    cursor = connection.cursor()
    error = False
    if request.method == 'POST':
        sql_query = "UPDATE  SET employees_name = '" + request.POST["name"] + "', address =  '" + request.POST["address"] + "', contact_information = " + request.POST["number"] + "',job_position =  " + request.POST["job_position"] + " WHERE employee_id = " + str(id)
        try:
            cursor.execute(sql_query)
        except:
            error = True
    cursor.execute("SELECT * FROM employees")
    results = cursor.fetchall()
    return render(request, 'employees.html', {'Employees': results, 'ERROR_UPDATE': error})


def showProductsNew(request):
    cursor = connection.cursor()
    error = False
    if request.method == 'POST':
        sql_query = "INSERT INTO products VALUES(" + request.POST["p_id"] +", '" + request.POST["name"] + "', '" +request.POST["description"] + "', '" + request.POST["number"]+"', " + request.POST["quantity"]+")"
        try :
            cursor.execute(sql_query)
        except :
            error = True
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()
    return render(request, 'products.html', {'Products': results, 'ERROR_INPUT': error})


def updateProduct(request,product_id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE product_id = " + str(product_id))
    product = cursor.fetchone()
    return render(request, 'products_update.html', {"Products": product})


def deleteProduct(request,product_id):
    cursor = connection.cursor()
    error = False
    sql_query = "DELETE FROM products WHERE product_id = " + str(product_id)
    try :
        cursor.execute(sql_query)
    except :
        error = True
        print("ERROR: SQL Query ->" + sql_query)
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()
    return render(request, 'products.html', {'Products': results, 'ERROR_DELETE': error})


def commitProductUpdate(request, id):
    cursor = connection.cursor()
    error = False
    if request.method == 'POST':
        sql_query = "UPDATE products SET product_name = '" + request.POST["name"] + "', description =  '" +request.POST["description"] + "', price = " + request.POST["number"] + ", quantity_in_stock =  " +request.POST["quantity"] + " WHERE product_id = " + str(id)
        try:
            cursor.execute(sql_query)
        except:
            error = True
            print("ERROR: SQL Query ->" + sql_query)
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()
    return render(request, 'products.html', {'Products': results, 'ERROR_UPDATE': error})


def showSuppliers(request):
    cursor = connection.cursor()
    error = False
    if request.method == 'POST':
        sql_query = "INSERT INTO suppliers VALUES(" + request.POST["s_id"] +", '" + request.POST["name"] + "', '" +request.POST["address"] + "', " + request.POST["number"]+")"
        try :
            cursor.execute(sql_query)
        except :
            error = True
    cursor.execute("SELECT * FROM suppliers")
    results = cursor.fetchall()
    return render(request, 'suppliers.html', {'Suppliers': results, 'ERROR_INPUT': error})


def deleteSupplier(request,supplier_id):
    cursor = connection.cursor()
    error = False
    sql_query = "DELETE FROM suppliers WHERE supplier_id = " + str(supplier_id)
    try:
        cursor.execute(sql_query)
    except :
         error = True
    cursor.execute("SELECT * FROM suppliers")
    results = cursor.fetchall()
    return render(request, 'suppliers.html', {'Suppliers': results, 'ERROR_DELETE': error})


def updateSupplier(request,supplier_id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM suppliers WHERE supplier_id = " + str(supplier_id))
    supplier = cursor.fetchone()
    return render(request, 'suppliers_update.html', {"Suppliers": supplier})


def commitSupplierUpdate(request, id):
    cursor = connection.cursor()
    error = False
    if request.method == 'POST':
        sql_query = "UPDATE suppliers SET supplier_name = '" + request.POST["name"] + "', address =  '" +request.POST["address"] + "', contact_information = " + request.POST["number"] + " WHERE supplier_id = " + str(id)
        try :
            cursor.execute(sql_query)
        except :
            error = True
    cursor.execute("SELECT * FROM suppliers")
    results = cursor.fetchall()
    return render(request, 'suppliers.html', {'Suppliers': results, 'ERROR_UPDATE': error})


def showSales(request):
    cursor = connection.cursor()
    cursor.execute("SELECT sale_id,customer_name,employee_name, sale_date, product_name, quantity_sold FROM sales NATURAL JOIN sale_items NATURAL JOIN (SELECT product_id, product_name   FROM products) AS a NATURAL JOIN (SELECT customer_id, customer_name FROM customers) AS b NATURAL LEFT JOIN (SELECT employee_name, employee_id FROM employees) AS c;")
    result = cursor.fetchall()
    return render(request, 'sale_report.html', {'SaleRecord':result})


def showInventoryReport(request):
    cursor = connection.cursor()
    cursor.execute("SELECT product_id, product_name, price, quantity_in_stock, quantity_sold, (price*quantity_sold) as revenue FROM products NATURAL LEFT JOIN (SELECT product_id, sum(quantity_sold) as quantity_sold FROM sale_items GROUP BY product_id) AS a ORDER BY revenue DESC;")
    result = cursor.fetchall()
    return render(request, 'inventory_report.html', {'InventoryReport': result})


def showEmployeeReport(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees NATURAL LEFT JOIN (SELECT employee_id, count(DISTINCT(sale_id))as number_of_sales, sum(revenue) AS cumulative_sales FROM sales NATURAL JOIN (SELECT sale_id, sum(price* quantity_sold) as revenue FROM sale_items NATURAL JOIN products GROUP BY sale_id) AS b GROUP BY employee_id) AS b;")
    result = cursor.fetchall()
    return render(request, 'employee_report.html', {'EmployeeReport': result})


def showSalesNew(request):
    cursor = connection.cursor()
    error = False
    if request.method == 'POST':

        if request.POST["employee_id"] == '':
            employee_id = "NULL"
        else:
            employee_id = str(request.POST["employee_id"])

        sql_query1 = "INSERT INTO sales VALUES(" + request.POST["sale_id"] + ", '" + request.POST["sale_date"]+ "', " + request.POST["customer_id"]+ ", " + employee_id +")"
        sql_query2 = "INSERT INTO sale_items (sale_id, product_id, quantity_sold) VALUES("+ request.POST["sale_id"]+ ", "+ request.POST["product_id"] + ", " +request.POST["quantity_sold"]+")"
        sql_query3 = "UPDATE products SET quantity_in_stock =quantity_in_stock - " + request.POST["quantity_sold"] + "  WHERE product_id = " + request.POST["product_id"]

        try:
            cursor.execute(sql_query3)
            cursor.execute(sql_query1)
            cursor.execute(sql_query2)
        except:
            print("ERROR : SQL Query -> " + sql_query1)
            print("ERROR : SQL Query -> " + sql_query2)
            error = True

        if not error and ("add_another_product" in request.POST) :
            return redirect("/sales/another_product/" + request.POST["sale_id"] )

    cursor.execute("SELECT sale_id,customer_name,employee_name, sale_date, product_name, quantity_sold, unique_id FROM sales NATURAL JOIN sale_items NATURAL JOIN (SELECT product_id, product_name   FROM products) AS a NATURAL JOIN (SELECT customer_id, customer_name FROM customers) AS b NATURAL LEFT JOIN (SELECT employee_name, employee_id FROM employees) AS c;")
    result = cursor.fetchall()
    return render(request, 'sales.html', {'SaleRecord': result, 'ERROR': error})


def addNewProductSALES(request, sale_id) :
    cursor = connection.cursor()
    error = False;
    if request.method == 'POST':
        sql_query = "INSERT INTO sale_items (sale_id, product_id, quantity_sold) VALUES(" + str(sale_id) + ", " + request.POST["product_id"] + ", " + request.POST["quantity_sold"] + ")"
        sql_query2 = "UPDATE products SET quantity_in_stock =quantity_in_stock - " + request.POST["quantity_sold"] + "  WHERE product_id = " + request.POST["product_id"]
        try:
            cursor.execute(sql_query2)
            cursor.execute(sql_query)
        except:
            print("ERROR : SQL Query -> " + sql_query)
            error = True
        if not error and ("commit_change" in request.POST):
            return redirect("/sales/")

    cursor.execute("SELECT * FROM sales WHERE sale_id = " + str(sale_id))
    result = cursor.fetchone()
    cursor.execute("SELECT sale_id,customer_name,employee_name, sale_date, product_name, quantity_sold, unique_id FROM sales NATURAL JOIN sale_items NATURAL JOIN (SELECT product_id, product_name   FROM products) AS a NATURAL JOIN (SELECT customer_id, customer_name FROM customers) AS b NATURAL LEFT JOIN (SELECT employee_name, employee_id FROM employees) AS c;")
    result1 = cursor.fetchall()
    return render(request, 'sales_add_another_product.html', {'SaleRecord': result1, "SALE": result, 'ERROR': error})


def deleteSale(request,unique_id,sale_id):
    cursor = connection.cursor()
    sql_query1 = "DELETE FROM sale_items WHERE unique_id = " + str(unique_id)
    sql_query2 = "SELECT COUNT(*) FROM sale_items WHERE sale_id = " + str(sale_id)
    sql_query3 = "DELETE FROM sales WHERE sale_id = " + str(sale_id)
    sql_query4 = "SELECT product_id, quantity_sold FROM sale_items WHERE unique_id = " + str(unique_id)

    cursor.execute(sql_query4)
    product_delete = cursor.fetchone()
    sql_query5 = "UPDATE products SET quantity_in_stock = quantity_in_stock + " + str(product_delete[1])+ " WHERE product_id = " + str(product_delete[0])
    cursor.execute(sql_query1)
    try :
        cursor.execute(sql_query5)
    except:
        print ("ERROR: SQL QUERY -> " + sql_query5)

    cursor.execute(sql_query2)
    if (cursor.fetchone()[0] == 0):
        cursor.execute(sql_query3)
    return redirect("/sales/")


def showPurchase(request):
    cursor = connection.cursor()
    error = False
    if request.method == 'POST':
        sql_query1 = "INSERT INTO purchases VALUES(" + request.POST["purchase_id"] + ", '" + request.POST["purchase_date"]+ "', " + request.POST["supplier_id"]+ ")"
        sql_query2 = "INSERT INTO purchase_items (purchase_id, product_id, quantity_purchased) VALUES("+ request.POST["purchase_id"]+ ", "+ request.POST["product_id"] + ", " +request.POST["quantity_purchased"]+")"
        sql_query3 = "UPDATE products SET quantity_in_stock =quantity_in_stock + " + request.POST["quantity_purchased"] + "  WHERE product_id = " + request.POST["product_id"]
        try:
            cursor.execute(sql_query1)
            cursor.execute(sql_query2)
            cursor.execute(sql_query3)
        except:
            print("ERROR : SQL Query -> " + sql_query1)
            print("ERROR : SQL Query -> " + sql_query2)
            error = True

        if not error and ("add_another_product" in request.POST) :
            return redirect("/purchases/another_product/" + request.POST["purchase_id"] )

    cursor.execute("SELECT purchase_id,product_name,supplier_name, purchase_date, quantity_purchased, unique_id FROM purchases NATURAL JOIN purchase_items NATURAL JOIN (SELECT product_id, product_name   FROM products) AS a NATURAL JOIN (SELECT supplier_id, supplier_name FROM suppliers) AS b")
    result = cursor.fetchall()
    return render(request, 'purchases.html', {'PurchaseRecord': result, 'ERROR': error})


def addNewProductPURCHASES(request, purchase_id) :
    cursor = connection.cursor()
    error = False
    if request.method == 'POST':
        sql_query1 = "INSERT INTO purchase_items (purchase_id, product_id, quantity_purchased) VALUES(" + str(purchase_id) + ", " + request.POST["product_id"] + ", " + request.POST["quantity_purchased"] + ")"
        sql_query2 = "UPDATE products SET quantity_in_stock =quantity_in_stock + " + request.POST["quantity_purchased"] + "  WHERE product_id = " + request.POST["product_id"]
        try:
            cursor.execute(sql_query2)
            cursor.execute(sql_query1)
        except:
            print("ERROR : SQL Query -> " + sql_query2)
            error = True

        if not error and ("commit_change" in request.POST) :
            return redirect("/purchases/")

    cursor.execute("SELECT * FROM purchases WHERE purchase_id = " + str(purchase_id))
    result = cursor.fetchone()
    cursor.execute("SELECT purchase_id,product_name,supplier_name, purchase_date, quantity_purchased, unique_id FROM purchases NATURAL JOIN purchase_items NATURAL JOIN (SELECT product_id, product_name   FROM products) AS a NATURAL JOIN (SELECT supplier_id, supplier_name FROM suppliers) AS b;")
    result1 = cursor.fetchall()
    return render(request, 'purchases_add_another_product.html', {'PurchaseRecord': result1, "PURCHASE": result, 'ERROR': error})


def deletePurchase(request , unique_id, purchase_id):
    cursor = connection.cursor()
    error = False
    sql_query1 = "DELETE FROM purchase_items WHERE unique_id = " + str(unique_id)
    sql_query2 = "SELECT COUNT(*) FROM purchase_items WHERE purchase_id = " + str(purchase_id)
    sql_query3 = "DELETE FROM purchases WHERE purchase_id = " + str(purchase_id)
    sql_query4 = "SELECT product_id, quantity_purchased FROM purchase_items WHERE unique_id = " +str(unique_id)

    cursor.execute(sql_query4)
    product_delete = cursor.fetchone()
    sql_query5 = "UPDATE products SET quantity_in_stock = quantity_in_stock - " +str(product_delete[1])+ " WHERE product_id = " + str(product_delete[0])
    try :
        cursor.execute(sql_query5)
    except:
        print("SQL Query :" + sql_query5)
        error = True

    if not error:
        cursor.execute(sql_query1)
        cursor.execute(sql_query2)
        if (cursor.fetchone()[0] == 0):
            cursor.execute(sql_query3)

    cursor.execute("SELECT purchase_id,product_name,supplier_name, purchase_date, quantity_purchased, unique_id FROM purchases NATURAL JOIN purchase_items NATURAL JOIN (SELECT product_id, product_name   FROM products) AS a NATURAL JOIN (SELECT supplier_id, supplier_name FROM suppliers) AS b;")
    result = cursor.fetchall()
    return render(request, 'purchases.html', {'PurchaseRecord': result, 'ERROR_DELETE': error})





