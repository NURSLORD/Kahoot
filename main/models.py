from django.db import models


# Create your models here.
class Players(models.Model):
    player_name = models.CharField(verbose_name='Имя', max_length=255)
    pin_code_player = models.PositiveBigIntegerField(verbose_name='PIN код')

    def __str__(self):
        return self.player_name

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


class Topics(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    pin_code = models.PositiveBigIntegerField(verbose_name='PIN код игры')
    player = models.OneToOneField(verbose_name='Учасник/ца', to=Players, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Questions(models.Model):
    topic_link = models.ForeignKey(verbose_name='Тема', to=Topics, on_delete=models.CASCADE)
    question = models.TextField(verbose_name='Вопрос')
    first_answer = models.CharField(verbose_name='1-ответ', max_length=255)
    second_answer = models.CharField(verbose_name='2-ответ', max_length=255)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
