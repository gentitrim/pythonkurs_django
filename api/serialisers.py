from rest_framework import serializers
from viewer.models import Movies

class MovieReadModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'


class MovieCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class MovieUpdatemodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        # exclude = ['id',"created"]
        fields = ['title','rated','description','released','genere']

