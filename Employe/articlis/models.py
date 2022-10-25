from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name= "Категория"


class Articles(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название статьи")
    text = models.TextField(max_length=200000, verbose_name="Текст статьи")
    author = models.CharField(max_length=50, verbose_name="Имя автора")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создание статьи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликованно")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Статьи"
        verbose_name= "Статья"


