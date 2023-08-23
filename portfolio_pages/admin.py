from django.contrib import admin
from .models import Project, Gallery, Blog


class CommentInline(admin.TabularInline):
    model = Gallery
    extra = 0 # por defecto muestra 3 espacios vacios

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]

# Register your models here.

admin.site.register(Project, ProjectAdmin)
admin.site.register(Gallery)
admin.site.register(Blog)