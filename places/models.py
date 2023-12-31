from django.db import models
from tinymce.models import HTMLField
from django.conf import settings


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.TextField(
        blank=True,
        verbose_name='Короткое описание'
    )
    description_long = HTMLField(
        blank=True,
        verbose_name='Полное описание'
    )
    lat = models.FloatField(
        verbose_name='Широта'
    )
    lon = models.FloatField(
        verbose_name='Долгота'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pk']


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Фотографии'
    )
    image = models.ImageField(upload_to=f'{settings.MEDIA_ROOT}')
    position = models.PositiveIntegerField('Позиция', default=0, blank=True)

    def __str__(self):
        return f'{self.pk} {self.place.title}'

    class Meta:
        ordering = ['position']
