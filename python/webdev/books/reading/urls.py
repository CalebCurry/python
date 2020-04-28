from django.urls import path

from . import views

app_name = 'reading'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.info, name='info'),
]