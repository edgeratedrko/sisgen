from django.urls import path
from .views import listAgenda, createAgendamento, updateAgendamento, deleteAgendamento

urlpatterns = [
    path('', listAgenda, name='listAgenda'),
    path('new', createAgendamento, name='createAgendamento'),
    path('update/<int:id>/', updateAgendamento, name='updateAgendamento'),
    path('delete/<int:id>/', deleteAgendamento, name='deleteAgendamento')
]