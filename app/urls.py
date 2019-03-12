from django.urls import path
from app import views

urlpatterns = [
	path('', views.home, name="home"),
	path('details/<int:id>/', views.detail, name="detail")
]
