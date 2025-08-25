from django.contrib import admin
from .models import (
    Project,Algorithm,Resume
)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','title','github_link','created_at']
    list_filter = ['created_at']
    search_fields = ['id','title']

@admin.register(Algorithm)
class AlgorithmAdmin(admin.ModelAdmin):
    list_display = ['id','title','github_link','created_at']
    list_filter = ['created_at']
    search_fields = ['id','title']

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id']