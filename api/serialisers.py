from rest_framework import serializers
from viewer.models import Movie

class MovieReadModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exluded = ['created']

        