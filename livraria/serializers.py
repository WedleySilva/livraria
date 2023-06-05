from rest_framework.serializers import ModelSerializer

from livraria.models import Autor, Categoria, CategoriaLivro, Editora, Livro

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = ["autores"]
        depth = 1

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class CategoriaLivroSerializer(ModelSerializer):
    class Meta:
        model = CategoriaLivro
        fields = "__all__"  

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1



