from django.urls import path

from . import views

urlpatterns = [
    path("", views.getAllBodyCompData, name="getAllBodyComp_view"),
    path("bodycomp/all", views.getAllBodyCompData, name="getAllBodyComp_view"),
    path("bodycomp/<str:pk>", views.getBodyCompData, name="getBodyComp_view"),
    path("bodycomp-add", views.addBodyCompData, name="addBodyComp_view"),
    path("bodycomp-update/<str:pk>", views.updateBodyCompData, name="updateBodyComp_view"),
    path("bodycomp-delete/<str:pk>", views.deleteBodyCompData, name="deleteBodyComp_view"),

]