from django.urls import path
from . import views
from blog import views as blog_views # Importa de nuestra app core 

urlpatterns = [
    path('', blog_views.blog, name="blog"),
    path('category/<int:category_id>/', blog_views.category, name="category"),

]
