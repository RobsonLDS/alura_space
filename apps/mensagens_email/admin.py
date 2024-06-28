from django.contrib import admin
from apps.mensagens_email.models import MensagensEmail

class ListandoMensagensEmail(admin.ModelAdmin):
    list_display = ("id", "edital", "edicao", "assunto")
    list_display_links = ("id", "edital")
    search_fields = ("edital",)
    list_filter = ("edital",)
    list_per_page = 10

admin.site.register(MensagensEmail, ListandoMensagensEmail)