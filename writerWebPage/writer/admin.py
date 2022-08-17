from django.contrib import admin
from .models import talent



# Register your models here.

class writerAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'email')
    search_fields =('fullName', 'email')
    list_filter = ('actor', 'announcer', 'singer', 'dancer' ,'writer', 'photographer')
    readonly_fields = ['talentPhoto',]

admin.site.register(talent, writerAdmin )