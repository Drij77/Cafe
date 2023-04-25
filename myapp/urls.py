from django.urls import path
from .views import create_address,address_list,create_location,search_cafes,edit_cafe,delete_cafe

urlpatterns = [
    path('create/', create_address, name='create_address'),
    path('', address_list, name='address_list'),
    path('locations/create/', create_location, name='create_location'),
    path('search/', search_cafes, name='search_cafes'),
    path('search/list/edit/<int:cafe_id>/', edit_cafe, name='edit_cafe'),
    path('search/list/delete/<int:cafe_id>/', delete_cafe, name='delete_cafe'),
]
