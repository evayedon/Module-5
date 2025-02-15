from django.urls import path
from . import views

urlpatterns = [
    # index or home page
    path('', views.post_list, name='post_list')
]