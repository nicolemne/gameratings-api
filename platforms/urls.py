from django.urls import path
from platforms import views

urlpatterns = [
    path('platforms/', views.PlatformList.as_view()),
]