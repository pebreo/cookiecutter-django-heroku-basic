from django.contrib import admin
from .models import {{ cookiecutter.model_name }}

class {{ cookiecutter.model_name }}Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title',]}
    list_display = ('title','time')
   
admin.site.register({{ cookiecutter.model_name }}, {{ cookiecutter.model_name }}Admin)