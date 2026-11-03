from django.db import models
class FotoPortifolio(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Titulo da Foto")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")

    # Alterado para URLField para armazenar o link direto retornado pelo Cloudinary (bypassa o limite do Vercel)
    imagem = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL da Foto")
    video = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL do Vídeo")

    data_publicacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Publicação")

    def __str__(self):
        return self.titulo




