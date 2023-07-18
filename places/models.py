from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    imgs = models.ImageField(
        blank=True,
        upload_to='images',
        verbose_name='Фото'
    )
    description_short = models.TextField(
        max_length=400,
        blank=True,
        verbose_name='Короткое описание'
    )
    description_long = models.TextField(
        blank=True,
        verbose_name='Полное описание'
    )
    lat = models.FloatField(
        blank=False,
        verbose_name='Широта'
    )
    lon = models.FloatField(
        blank=False,
        verbose_name='Долгота'
    )

    def __str__(self):
        return self.title
