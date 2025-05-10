from django.urls import path
from . import views
from core import views as core_views # Importa de nuestra app core 

urlpatterns = [
    path('', core_views.home, name="home"),
    path('about/', core_views.about, name="about"),
    path('store/', core_views.store, name="store"),
]
