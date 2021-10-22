from django.urls import path
from .views import listarUser, createUser, updateUser, deleteUser

urlpatterns = [
    path('', listarUser, name='listarUser'),
    path('newuser', createUser, name='createUser'),
    path('update/<int:id>/', updateUser, name='updateUser'),
    path('delete/<int:id>/', deleteUser, name='deleteUser'),
    
]