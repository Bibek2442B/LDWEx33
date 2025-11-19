from django.urls import path
from .views import ProductListView

app_name = "products"
urlpatterns = [
    # path("request-info/", RequestExplorerView.as_view(), name="request_info"),
    path("", ProductListView.as_view(), name="products")
]