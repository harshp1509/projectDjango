from django.forms import ModelForm
from app.models import Suggestion

class SuggestionForm(ModelForm):
    class Meta:
        model=Suggestion
        fields = ['Subject','Description']
