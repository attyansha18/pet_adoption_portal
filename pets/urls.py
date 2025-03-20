from django.urls import path
from .views import pet_list, pet_detail, add_pet

urlpatterns = [
    path('', pet_list, name='pet_list'),
    path('<int:pet_id>/', pet_detail, name='pet_detail'),
    path('add/', add_pet, name='add_pet'),
]
