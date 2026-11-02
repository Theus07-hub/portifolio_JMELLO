from django.contrib import admin
from .models import FotoPortifolio

@admin.register(FotoPortifolio)
class FotoPortifolioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo',)
