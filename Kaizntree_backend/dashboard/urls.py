from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("addItem", views.addItem, name="addItem"),
    path("category", views.category, name="category"),
    path("tag", views.tag, name="tag"),
    path("filterByName", views.filterByName, name="filterByName"),
    path("filterByStatus", views.filterByStatus, name="filterByStatus"),
    path("filterByDate", views.filterByDate, name="filterByDate"),

]
