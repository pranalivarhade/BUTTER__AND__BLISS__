from django.contrib import admin
from django.urls import path
from .views import home, product_list, add_product
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.product_list, name="product_list"),
    path("products/<int:product_id>/", views.product_detail, name="product_detail"),
    path("add-product/", views.add_product, name="add_product"),
    path("logout/", views.logout_view, name="logout"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),

   path("cart/", views.cart, name="cart"),
path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
path("delete-product/<int:product_id>/", views.delete_product, name="delete_product"),

path("edit-product/<int:product_id>/", views.edit_product, name="edit_product"),

path("remove-from-cart/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
path("increase-qty/<int:item_id>/", views.increase_qty, name="increase_qty"),
path("decrease-qty/<int:item_id>/", views.decrease_qty, name="decrease_qty"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
