from rest_framework.serializers import ModelSerializer

from livraria.models import Autor, Categoria, Editora, Livro

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = ["autores"]
        depth = 1

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"


