from django import forms
from ghostpostApp.models import ghostpost


class submit_ghostpost(forms.ModelForm):
    class Meta:
        model = ghostpost
        fields = ['ghostpost_choice', 'ghostpost_content']
