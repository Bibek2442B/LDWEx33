from django.urls import path
from .views import  ProductAdminCreate, ProductAdminDelete, ProductAdminListView, ProductAdminUpdate, ProductListView, CategoryAdminListView, CategoryAdminCreate, CategoryAdminUpdate, CategoryAdminDelete

app_name = "products"
urlpatterns = [
    # path("request-info/", RequestExplorerView.as_view(), name="request_info"),
    path("", ProductListView.as_view(), name="products"),
    path("admin/categories/", CategoryAdminListView.as_view(), name="admin_categories"),
    path("admin/categories/add/", CategoryAdminCreate.as_view(), name="admin_category_add"),
    path("admin/categories/<int:pk>/edit/", CategoryAdminUpdate.as_view(), name="admin_category_edit"), 
    path("admin/categories/<int:pk>/delete/", CategoryAdminDelete.as_view(), name="admin_category_delete"),
    path("admin/products/", ProductAdminListView.as_view(), name="admin_products"),
    path("admin/products/add/", ProductAdminCreate.as_view(), name="admin_product_add"),
    path("admin/products/<int:pk>/edit/", ProductAdminUpdate.as_view(), name="admin_product_edit"), 
    path("admin/products/<int:pk>/delete/", ProductAdminDelete.as_view(), name="admin_product_delete"),
]