from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.Add.as_view(),name="add db"),
]