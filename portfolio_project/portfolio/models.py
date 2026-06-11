from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Loyiha nomi")
    description = models.TextField(verbose_name="Tavsif")
    image = models.ImageField(upload_to='projects/', verbose_name="Rasm")
    link = models.URLField(verbose_name="Loyiha havolasi", blank=True)

    def __str__(self):
        return self.title