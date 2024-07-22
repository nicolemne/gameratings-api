from django.urls import path
from saved_games import views

urlpatterns = [
    path("saved_games/", views.SavedGameList.as_view()),
    path("saved_games/<int:pk>/", views.SavedGameDetail.as_view()),
]
