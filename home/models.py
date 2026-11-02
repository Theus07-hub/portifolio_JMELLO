from django.db import models
class FotoPortifolio(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Titulo da Foto")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    imagem = models.ImageField(upload_to='portifolio_fotos/', verbose_name="Arquivo da Foto")
    video = models.FileField(upload_to='portifolio_fotos/', blank=True, null=True, verbose_name="Arquivo de Vídeo")
    data_publicacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Publicação")

    def __str__(self):
        return self.titulo




