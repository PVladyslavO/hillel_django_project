from django.urls import path
from api.views.homework_querysets import homework_querysets

urlpatterns = [
    path("homework-querysets/", homework_querysets, name="homework_querysets"),
]
