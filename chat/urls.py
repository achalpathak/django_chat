from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("agent_portal/", views.select_role, name="select_role"),
]
