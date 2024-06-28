from django.forms import ModelForm
from apps.mensagens_email.models import MensagensEmail

class MensagensEmailForm(ModelForm):
    class Meta:
        model = MensagensEmail
        fields = '__all__'