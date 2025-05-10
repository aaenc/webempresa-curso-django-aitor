from django.urls import path
from . import views
from contact import views as contact_views # Importa de nuestra app contact 

urlpatterns = [
    path('', contact_views.contact, name="contact"),
]
