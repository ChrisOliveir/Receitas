from django.contrib import admin

from .models import Receitas

class ReceitasAdmin(admin.ModelAdmin):
    list_display = ('nome_receita','ingredientes','modo_preparo')

admin.site.register(Receitas, ReceitasAdmin)
