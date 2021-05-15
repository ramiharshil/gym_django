

from django.forms import ModelForm

from .models import clientdetails


class clientsform(ModelForm):
    class Meta:
        model = clientdetails
        fields = ['name', 'gender', 'packagep', 'packages', 'packagee', 'feesp', 'tranningtype']
