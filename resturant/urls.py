from django.urls import path
from . import views

app_name = 'resturant'

urlpatterns = [
    path('', views.MenuList.as_view(), name='index'),
    path('dish/<int:pk>/', views.MenuDetail.as_view(), name='dish_detail'),
]
