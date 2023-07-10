from .views import DeafultView
from django.urls import path

urlpatterns = [
    path('welcome', DeafultView.as_view())
]
