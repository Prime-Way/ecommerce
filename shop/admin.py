from django.contrib import admin
from .models import *


# Register your models here.

class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


admin.site.register(categ, CatAdmin)


class ProdAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


admin.site.register(product, ProdAdmin)
