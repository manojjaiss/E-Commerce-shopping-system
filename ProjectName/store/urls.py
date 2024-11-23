# Project-level urls.py
from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("success/", views.success, name="success"),
    path("cancel/", views.cancel, name="cancel"),
]
