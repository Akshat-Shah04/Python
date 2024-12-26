# ProductManagement/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add_product/", views.add_product, name="add_product"),
    path("add_subcategory/", views.add_subcategory, name="add_subcategory"),
    path(
        "update_subcategory/<int:pk>/",
        views.update_subcategory,
        name="update_subcategory",
    ),
    path(
        "delete_subcategory/<int:pk>/",
        views.delete_subcategory,
        name="delete_subcategory",
    ),
    path("update_product/<int:pk>/", views.update_product, name="update_product"),
    path("delete_product/<int:pk>/", views.delete_product, name="delete_product"),
    path("search_product/", views.search_product, name="search_product"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
