from django.forms import Form,CharField,IntegerField,DateField,Textarea,ModelChoiceField,ModelForm
from .models import Genere,Movies
from django.core.exceptions import ValidationError

class MovieForm(Form):
    title = CharField(max_length=128)
    rated = IntegerField(min_value=1,max_value=10)
    released = DateField()
    description = CharField(widget=Textarea)
    genere = ModelChoiceField(Genere.objects)
    
    def clean_title(self):
        return self.cleaned_data["title"].capitalize()

    def clean_rating(self):
        if self.cleaned_data['rated'] < 3:
            raise ValidationError("The rating must be more than 3")
        return self.cleaned_data['rated']

    def clean(self):
        if self.cleaned_data['genere'].name == 'action' and self.cleaned_data['rated'] >= 8:
            raise ValidationError('Action movies must have rating lower than 9')
        return super().clean()
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'
    
class MovieModelForm(ModelForm):
    class Meta:
        model = Movies
        fields = "__all__"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'



class DirectorForm(Form):
    name = CharField(max_length=128)
    surname = CharField(max_length=128)

    def clean_name(self):
        return self.cleaned_data["name"].capitalize()
    
    def clean_surname(self):
        return self.cleaned_data["surname"].capitalize()
    

