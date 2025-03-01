from django.db import models
from django.db.models import CharField,IntegerField,DateTimeField,TextField,ForeignKey,DateField,DO_NOTHING

# Create your models here.

class Genere(models.Model):
    name = CharField( max_length=50)

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name
    

class Movies(models.Model):
    title = CharField(max_length=128)
    rated = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)
    genere = ForeignKey("Genere",on_delete=DO_NOTHING)

    def __str__(self):
        return f"Movie name: {self.title}-{self.released}"
    
    def __repr__(self):
        return f"Movie name: {self.title}-{self.released}"
    

class Director(models.Model):
    name = CharField(max_length=128)
    surname = CharField(max_length=128)

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __repr__(self):
        return f'{self.name} {self.surname}'
    
