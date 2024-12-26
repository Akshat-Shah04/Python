from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.db.models import Q
from .models import *


# Login View
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pin = request.POST.get("pin")
        employee = Employee.objects.get(email=email, pin=pin)
        if employee:
            request.session["email"] = employee.email
            request.session["role"] = employee.role
            if request.session["role"] == "Admin":
                return redirect("admin_dashboard")
            else:
                return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid email or password"})
    return render(request, "login.html")


# Logout View
def logout(request):
    request.session.flush()
    return redirect("login")


# Admin Dashboard
def admin_dashboard(request):
    if request.session.get("role") != "Admin":
        return HttpResponseForbidden("You are not authorized to view this page.")
    products = ProductMst.objects.all()
    return render(request, "admin_dashboard.html", {"products": products})


# Add Product
def add_product(request):
    if request.session.get("role") != "Admin":
        return HttpResponseForbidden("You are not authorized to view this page.")
    if request.method == "POST":
        pname = request.POST.get("pname")
        ProductMst.objects.create(pname=pname)
        return redirect("admin_dashboard")
    return render(request, "add_product.html")


# Add Subcategory
def add_subcategory(request):
    if request.session.get("role") != "Admin":
        return HttpResponseForbidden("You are not authorized to view this page.")
    products = ProductMst.objects.all()
    if request.method == "POST":
        product_id = request.POST.get("product")
        price = request.POST.get("price")
        model = request.POST.get("model")
        ram = request.POST.get("ram")
        image = request.FILES.get("image")
        product = get_object_or_404(ProductMst, pk=product_id)
        ProductSubCat.objects.create(
            product=product, price=price, model=model, ram=ram, image=image
        )
        return redirect("admin_dashboard")
    return render(request, "add_subcategory.html", {"products": products})


# Update Product
def update_product(request, pk):
    if request.session.get("role") != "Admin":
        return HttpResponseForbidden("You are not authorized to view this page.")
    product = get_object_or_404(ProductMst, pk=pk)
    if request.method == "POST":
        product.pname = request.POST.get("pname")
        product.save()
        return redirect("admin_dashboard")
    return render(request, "update_product.html", {"product": product})


# Delete Product
def delete_product(request, pk):
    if request.session.get("role") != "Admin":
        return HttpResponseForbidden("You are not authorized to view this page.")
    product = get_object_or_404(ProductMst, pk=pk)
    product.delete()
    return redirect("admin_dashboard")


# Product Manager Dashboard
def dashboard(request):
    if request.session.get("role") not in ["Admin", "Product Manager"]:
        return HttpResponseForbidden("You are not authorized to view this page.")
    subcategories = ProductSubCat.objects.all()
    return render(request, "dashboard.html", {"subcategories": subcategories})


# Search Product
def search_product(request):
    if request.session.get("role") not in ["Admin", "Product Manager"]:
        return HttpResponseForbidden("You are not authorized to view this page.")
    query = request.GET.get("q")
    subcategories = (
        ProductSubCat.objects.filter(
            Q(product__pname__icontains=query) | Q(model__icontains=query)
        )
        if query
        else ProductSubCat.objects.all()
    )
    return render(request, "dashboard.html", {"subcategories": subcategories})


def update_subcategory(request, pk):
    subcategory = get_object_or_404(ProductSubCat, pk=pk)

    if request.method == "POST":
        subcategory.pname = request.POST["pname"]
        subcategory.price = request.POST["price"]
        subcategory.model = request.POST["model"]
        subcategory.image = request.FILES["image"]
        subcategory.ram = request.POST["ram"]
        subcategory.save()
        return redirect("dashboard")  # Redirect back to the product manager's dashboard
    else:
        return render(request, "update_subcategory.html", {"subcategory": subcategory})


def delete_subcategory(request, pk):
    subcategory = get_object_or_404(ProductSubCat, pk=pk)
    subcategory.delete()
    return redirect("dashboard")
