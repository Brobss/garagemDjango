from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from garagem.models import Marca, Categoria, Cor, Acessorio, Veiculo
from garagem.serializers import MarcaSerializer, CategoriaSerializer, CorSerializer, AcessorioSerializer, VeiculoSerializer, VeiculoDetailSerializer, VeiculoListSerializer











