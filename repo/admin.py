from django.contrib import admin
from .models import Profile,Projects,Review

# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted',)

admin.site .register(Projects)
admin.site .register(Review)