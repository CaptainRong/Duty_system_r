from django.urls import path
from index import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download/', views.download, name='download')
]
