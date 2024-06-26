from django.urls import path
from . import views

urlpatterns = [
    path('ratings/', views.RatingListCreate.as_view(), name='rating-list-create'),
    path('ratings/<int:pk>/', views.RatingRetrieveUpdateDestroy.as_view(), name='rating-retrieve-update-destroy'),
]
