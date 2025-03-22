from django.contrib import admin
from viewer.models import Genere,Movies


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','rated','released','description','genere']
    list_filter = ['genere','rated']
    search_fields = ['title','description']

# Register your models here.
admin.site.register(Movies,MovieAdmin)
admin.site.register(Genere)