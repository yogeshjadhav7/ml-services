from django.urls import path, include
from . import views

urlpatterns = [
    path('predict/', views.predict, name="predict"),
    path('train/', views.train, name="train")
]