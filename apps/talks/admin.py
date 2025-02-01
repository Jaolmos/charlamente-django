from django.contrib import admin
from .models import Talk

@admin.register(Talk)
class TalkAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'speaker')
    readonly_fields = ('created_at', 'updated_at')
