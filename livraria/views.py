from rest_framework.viewsets import ModelViewSet

from livraria.models import Autor, Categoria, CategoriaLivro, Editora, Livro
from livraria.serializers import AutorSerializer, CategoriaSerializer, CategoriaLivroSerializer, EditoraSerializer, LivroSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaLivroViewSet(ModelViewSet):
    queryset = CategoriaLivro.objects.all()
    serializer_class = CategoriaLivroSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


