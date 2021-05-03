from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPers
from .forms import UsuarioPersCreationForm, UsuarioPersChangeForm

# Register your models here.
#creacion y visualizacion del usuario personalizado
class UsuarioPersAdmin(UserAdmin):
    model = UsuarioPers
    list_display = ['email', 'username', 'edad' , 'telefono','genero', 'is_staff',]

#registro de los modelos para poder visualizarlos el admin
admin.site.register(UsuarioPers,UsuarioPersAdmin)