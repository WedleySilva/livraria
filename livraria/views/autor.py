from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from livraria.models import Autor
from livraria.serializers.livro import AutorSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [IsAuthenticated]