from django.contrib import admin
from templatesApp.models import User 
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido' ,'cargo' , 'email', 'fono', 'direccion']


admin.site.register(User, UserAdmin)

