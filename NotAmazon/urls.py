from django.urls import path

from . import views

urlpatterns = [
    path("home", views.index, name="index"),
    path("products", views.products, name="products"),
    path("shop", views.shop, name="shop"),
    path("user_login", views.user_login, name="user_login"),
    path("user_signup", views.user_signup, name="user_signup"),
]
