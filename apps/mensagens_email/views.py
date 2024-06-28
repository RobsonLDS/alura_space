from django.shortcuts import render
from apps.mensagens_email.models import MensagensEmail
from apps.mensagens_email.forms import MensagensEmailForm

def post_mensagens(request):
    data = MensagensEmail.objects.all()
    
    form = MensagensEmailForm
    if request.method == 'POST':
        form = MensagensEmailForm(request.POST)
        if form.is_valid:
            form.save()
            form = MensagensEmailForm

    context={"data": data, "form": form}
    return render(request, "mensagens_email.html", context)