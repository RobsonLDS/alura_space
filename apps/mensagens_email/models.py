from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import logging

logger = logging.getLogger(__name__)
# Create your models here.
class MensagensEmail(models.Model):

    usuario = models.ForeignKey(to="auth.user", on_delete=models.CASCADE, null=True)
    edital = models.IntegerField(null=False, default=False)
    edicao = models.IntegerField(null=False, default=False)
    atividade = models.CharField(max_length=5, null=True, blank=True)

    dest_administrador = models.BooleanField(null=False, default=False)
    dest_comissao = models.BooleanField(null=False, default=False)
    dest_solicitante = models.BooleanField(null=False, default=False)
    dest_orientador = models.BooleanField(null=False, default=False)
    dest_coordenador = models.BooleanField(null=False, default=False)
    dest_outros = models.BooleanField(null=False, default=False)

    para = models.CharField(max_length=255, null=True, blank=True)
    assunto = models.CharField(max_length=255, null=True, blank=True)

    mensagem = RichTextUploadingField()
    data = models.DateField(null=True, blank=True)
    hora = models.TimeField(null=True, blank=True)

    def __str__(self):
        return 'Mensagem Assunto ' + str(self.assunto)

    def get_atividade_mensagem(self):
        if self.atividade == 'ANDA':
            return 'Em andamento - Período de Inscrição'
        if self.atividade == 'COMI':
            return 'Avaliação das propostas - Comissão ou Aguardando Anuência'
        if self.atividade == 'RELA':
            return 'Apresentação do relatório técnico - Aguardando Relatório'

    def set_edital(self, edital):
        self.edital = edital