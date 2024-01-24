from django.urls import include, path

from . import views

app_name = "products"
urlpatterns = [
    path("", views.products_list, name="list"),
]
