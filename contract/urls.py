from django.urls import path
from . import views

app_name = 'contract'
urlpatterns = [
    path('',views.contrac.as_view(),name='contract'),
]