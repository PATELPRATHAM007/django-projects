from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<int:month>", views.monthly_challenge_by_index, name="monthly_challenge_by_index"),
    path("<str:month>", views.monthly_challenge, name="monthly_challenge"),
]
