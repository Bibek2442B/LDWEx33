from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Category
from .forms import CategoryForm

class RequestExplorerView(View):
    def get(self, request):
        # query params: /shop/products/request-info/?page=2&order=desc
        query_params = dict(request.GET)
        page = request.GET.get("page")
        method = request.method
        path = request.path
        user = request.user.username if request.user.is_authenticated else "anonymous"
        client_ip = request.META.get("REMOTE_ADDR")
        user_agent = request.META.get("HTTP_USER_AGENT", "")

        lines = [
            f"Method: {method}",
            f"Path: {path}",
            f"User: {user}",
            f"Query params: {query_params}",
            f"Page param: {page}",
            f"Client IP: {client_ip}",
            f"User-Agent: {user_agent}",
        ]
        return HttpResponse("\n".join(lines), content_type="text/plain")


class ProductListView(View):
    def get(self, request):
        products = [
            {"name": '24" Monitor', "price": 129.90, "available": True},
            {"name": "Mechanical Keyboard", "price": 89.50, "available": False},
            {"name": "Wireless Mouse", "price": 29.99, "available": True},
        ]
        context = {
            "products": products,
        }
        return render(request, "products/list.html", context)
    
class CategoryAdminListView(ListView):
    model = Category
    template_name = "products/categories/admin_list.html"
    context_object_name = "categories"
    paginate_by = 10

class CategoryAdminCreate(CreateView):
    form_class = CategoryForm
    template_name = "products/categories/admin_form.html"
    success_url = reverse_lazy("products:admin_categories")

class CategoryAdminUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "products/categories/admin_form.html"
    success_url = reverse_lazy("shop:products:admin_categories")

class CategoryAdminDelete(DeleteView):
    model = Category
    template_name = "products/categories/admin_confirm_delete.html"
    success_url = reverse_lazy("shop:products:admin_categories")
