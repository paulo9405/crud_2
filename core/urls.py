from django.urls import path
from .views import lista_pessoas, nova_pesssoa, update_pessoa


urlpatterns = [
    path('', lista_pessoas, name='lista_pessoas'),
    path('nova-pessoa', nova_pesssoa, name='nova_pessoa'),
    path('update-pessoa/<int:id>', update_pessoa, name='update_pessoa'),

]