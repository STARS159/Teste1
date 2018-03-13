from django.contrib import admin
from .models import Pessoa
from .models import EventoCientifico
from .models import Autor 
from .models import PessoaJuridica
from .models import PessoaFisica
from .models import Evento 
from .models import ArtigoCientifico

# Register your models here.

admin.site.register(Pessoa)
admin.site.register(EventoCientifico)
admin.site.register(Autor)
admin.site.register(PessoaJuridica)
admin.site.register(PessoaFisica)
admin.site.register(Evento)
admin.site.register(ArtigoCientifico)