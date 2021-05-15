from django.urls import path
from . import views

urlpatterns = [

        path('', views.addclients, name='addclients'),
        path('view_clients', views.view_clients, name='view_clients'),
        path('dob', views.dob, name='dob'),
        path('renewald', views.renewald, name='renewald'),
        path('edit/<int:id>/', views.edit, name='edit'),
        # path('update/<int:id>/', views.update, name='update')
]