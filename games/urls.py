from django.urls import path
from games import views

urlpatterns = [
    path('games/', views.GameList.as_view()),
    path('games/<int:pk>/', views.GameDetail.as_view()),
]
