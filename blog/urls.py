from . import views
from django.urls import path

urlpatterns = [
    path('', views.postList, name="home"),
    path('<slug:slug>/', views.postDetail, name='post_detail'),
]
