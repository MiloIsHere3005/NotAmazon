from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.index, name="home"),
    path("products/", views.products, name="products"),
    path("shop/", views.shop, name="shop"),
    path("registration/login/", views.login, name="login"),
    path("registration/signup/", views.signup, name="signup"),
]
