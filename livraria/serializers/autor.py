from rest_framework.serializers import ModelSerializer
from livraria.models import Autor

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = ["autores"]
        depth = 1