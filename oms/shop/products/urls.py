from django.urls import path
from .views import ProductListView, CategoryAdminListView

app_name = "products"
urlpatterns = [
    # path("request-info/", RequestExplorerView.as_view(), name="request_info"),
    path("", ProductListView.as_view(), name="products"),
    path("admin/categories/", CategoryAdminListView.as_view(), name="admin_categories"),
]