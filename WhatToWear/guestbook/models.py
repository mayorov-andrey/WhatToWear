from django.db import models


class GuestBook(models.Model):
    user = models.CharField(max_length=20, verbose_name="Пользователь")
    posted = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    content = models.TextField(verbose_name="Содержание")

    class Meta:
        ordering = ["-posted"]
        verbose_name = "запись гостевой книги"
        verbose_name_plural = "записи гостевой книги"
