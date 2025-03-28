from django.urls import path
from . import views

urlpatterns = [
    path('reviews/product/<int:product_id>/add-review/', views.add_review, name='add_review')

]