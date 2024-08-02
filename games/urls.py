from django.urls import path
from games import views

urlpatterns = [
    path('games/', views.GameList.as_view()),
    path('games/<slug:slug>/', views.GameDetail.as_view()),
]
