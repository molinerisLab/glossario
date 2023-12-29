from django.forms import ModelForm
from .models import Customer

class CustomerForm(ModelForm):#http://stackoverflow.com/questions/454436/unique-fields-that-allow-nulls-in-django
    class Meta:
        model = Customer
        fields = '__all__'
    def clean_email(self):
        return self.cleaned_data['email'] or None
