from django.db import models
from django.contrib.auth.models import User
import NoteService.settings as settings
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name='Название категории')


class Note(models.Model):
    def __str__(self):
        return self.title + ' (' + str(self.date) + ') '
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Содержимое')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    mark = models.BooleanField(verbose_name='Избранная')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, verbose_name='Владелец записи', on_delete=models.CASCADE)


# Create your models here.
