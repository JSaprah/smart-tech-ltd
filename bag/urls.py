from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path(
        'add/<product_id>/',
        views.add_product_to_bag,
        name='add_product_to_bag'
        ),
    path('update/<product_id>/', views.update_bag, name='update_bag'),
]
