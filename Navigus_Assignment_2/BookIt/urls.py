from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('create-slot/', views.createSlot, name='createSlot'),
    path('view-slot/', views.viewSlot, name='viewSlot'),
    path('api/book/', views.bookSlot, name='bookSlot'),
    path('api/remove/', views.removeSlot, name='removeSlot'),
    path('api/', include(('BookIt.api.urls','BookIt'),namespace='api-slot-web')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_web')),
   ]