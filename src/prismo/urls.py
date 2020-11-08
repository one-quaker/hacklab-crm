from django.urls import path
from django.conf import settings
from prismo import views


urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index-view'),
]
