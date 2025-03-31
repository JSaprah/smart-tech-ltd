from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/add-review/', views.add_review, name='add_review'),
    path('product/<int:review_id>/delete-review/', views.delete_review, name='delete_review'),
    path('product/<int:review_id>/edit-review/', views.edit_review, name='edit_review'),
]