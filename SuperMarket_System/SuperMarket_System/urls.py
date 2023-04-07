"""
URL configuration for SuperMarket_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showProducts),
    path('customers/', views.showCustomers),
    path('customers/delete_customer/<int:customer_id>', views.deleteCustomer),
    path('customers/update_customer/<int:customer_id>', views.updateCustomer),
    path('customers/update_commit/<int:id>', views.commitUpdate),

    path('employees/', views.showEmployees),
    path('employees/delete_employee/<int:employee_id>', views.deleteEmployees),
    path('employees/update_employee/<int:employee_id>', views.updateEmployees),
    path('employees/update_commit/<int:id>', views.commitEmpUpdate),

    path('products/', views.showProductsNew),
    # path('products/delete_product/<int:product_id>', views.deleteProduct),
    # path('customers/update_product/<int:product_id>', views.updateProduct),
    # path('products/update_commit/<int:id>', views.commitProductUpdate),

    path('sale_report/', views.showSales),
    path('inventory_report/', views.showInventoryReport),
    path('employee_report/', views.showEmployeeReport),
]
