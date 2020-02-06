from django.db import models
from datetime import datetime


class New(models.Model):
    title = models.CharField(max_length=100, unique_for_date="posted", verbose_name="Заголовок")
    description = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Опубликована")

    class Meta:
        ordering = ["-posted"]
        verbose_name = "новость"
        verbose_name_plural = "новости"