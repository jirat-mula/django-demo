from django.urls import path,include

from . import views

urlpatterns = [
    path('view/',views.viewdata,name='viewdata'),
    path('',views.Add.as_view(),name="add db"),
    path('store/',views.store_proc,name="store"),
]