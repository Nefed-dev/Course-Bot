from django.db import models


# Create your models here.

class TimeBaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(TimeBaseModel):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(verbose_name='ID пользователя телеграмм', unique=True, default=1) # Телеграм ID
    name = models.CharField(verbose_name='Имя пользователя', max_length=100)
    username = models.CharField(verbose_name='Username TG', max_length=100, null=True)

    def __str__(self):
        return f'№{self.id} - {self.user_id} - {self.name}'

class Item(TimeBaseModel):
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Название урока', max_length=50)
    description = models.TextField(verbose_name='Описание', max_length=100)

    # homework, cheatsheet, workbook, check-list

    category_code = models.CharField(verbose_name='Код категории', max_length=20)
    category_name = models.CharField(verbose_name='Название категории', max_length=20)
    subcategory_code = models.CharField(verbose_name='Код подкатегории', max_length=20)
    subcategory_name = models.CharField(verbose_name='Название подкатегории', max_length=20)

    def __str__(self):
        return f'№{self.id} - {self.name}'
