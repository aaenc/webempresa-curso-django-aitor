from django.urls import path
from pages import views as page_views # Importa de nuestra app core 

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>', page_views.page, name="page"),
]
