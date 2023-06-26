from rest_framework.serializers import ModelSerializer
from livraria.models import Livro
from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .editora import EditoraSerializer

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"

class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1