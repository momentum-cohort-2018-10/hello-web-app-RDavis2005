from django.forms import ModelForm
from collection.models import Jersey

class JerseyForm(ModelForm):
    class Meta:
        model = Jersey #based on the Jersey model
        fields = ('name', 'description',) #Only allows you to update the name and description