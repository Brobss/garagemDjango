from django.contrib import admin

from .models import Marca
from .models import Categoria
from .models import Cor
from .models import Acessorio
from .models import Veiculo

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Cor)
admin.site.register(Acessorio)
admin.site.register(Veiculo)