from .views import TestListApiView
from django.urls import path

urlpatterns = [
    path('test/',TestListApiView.as_view())
]
