from django.contrib import admin
from .models import Album

@admin.register(Album)
class Album(admin.ModelAdmin):
      list_display = ('name','description')