from django.contrib import admin
from .models import Post, Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('Sensor', 'Tpye', 'Time','Data',)
    search_fields = ('Sensor', 'Tpye', 'Time','Data',)

# Register your models here.
# admin.site.register(Post)
admin.site.register(Article, ArticleAdmin)


