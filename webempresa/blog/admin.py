from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    # Para mostrar mas columnas en el listado (nombre del campo en el modelo)
    list_display = ('name',)

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    # Para mostrar mas columnas en el listado (nombre del campo en el modelo)
    list_display = ('title','author', 'post_published','post_categories')
    ordering = ('author','published')
    search_fields = ('title','content','author__username','categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name')

    def post_categories(self,obj):
        return ", ".join(c.name for c in obj.categories.all().order_by('name'))

    def post_published(self,obj):
        return obj.published.strftime('%d/%m/%Y %H:%M')
    
    # Para ponerle un nombre a una columna
    post_categories.short_description="Categorías"
    post_published.short_description="F.Publicación"

admin.site.register(Category,CategoryAdmin)

admin.site.register(Post,PostAdmin)
