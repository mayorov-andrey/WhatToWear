from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True, unique=True, verbose_name="Название")
    order = models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name="Порядковый номер")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
