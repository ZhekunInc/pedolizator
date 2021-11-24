from django.db import models
from django.utils import timezone

# Create your models here.


class TimeStampModel(models.Model):

    is_published = models.BooleanField(
        default=True, verbose_name=('published')
    )
    published_at = models.DateTimeField(
        ("published at"), default=timezone.now
    )
    created_at = models.DateTimeField(("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(('updated at'), auto_now=True)

    class Meta:
        abstract = True


class Season(TimeStampModel):

    title = models.CharField(
        verbose_name=('Title'), max_length=512, db_index=True
    )
    slug = models.SlugField(
        verbose_name=('Slug'), max_length=512, db_index=True, unique=True
    )
    is_archive = models.BooleanField(
        ("Is arhive season?"), default=False
    )

    class Meta:
        verbose_name = ("season")
        verbose_name_plural = ("seasons")

    def __str__(self):
        return self.title


class Stage(TimeStampModel):

    title = models.CharField(
        verbose_name=('Title'), max_length=512, db_index=True
    )
    slug = models.SlugField(
        verbose_name=('Slug'), max_length=512, db_index=True, unique=True
    )
    season = models.ForeignKey(
        'Season', related_name='stage',
        verbose_name=('season'), on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = ("stage")
        verbose_name_plural = ("stages")

    def __str__(self):
        return self.title


class Match(TimeStampModel):

    title = models.CharField(
        verbose_name=('Title'), max_length=512, db_index=True
    )
    slug = models.SlugField(
        verbose_name=('Slug'), max_length=512, db_index=True, unique=True
    )
    result_1 = models.PositiveIntegerField(
        verbose_name='First team score:'
    )
    result_2 = models.PositiveIntegerField(
        verbose_name='Second team score:'
    )
    stage = models.ForeignKey(
        'stage', related_name='match',
        verbose_name=('stage'), on_delete=models.CASCADE,
    )
    end_at = models.DateTimeField(
        ("This match will start at"), default=timezone.now
    )

    class Meta:
        verbose_name = ("match")
        verbose_name_plural = ("matches")

    def __str__(self):
        return self.title


class Forecast(TimeStampModel):

    match = models.ForeignKey(
        'match', related_name='forecast',
        verbose_name=('match'), on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'auth.User', related_name='forecast',
        verbose_name=('user'), on_delete=models.CASCADE,
    )
    forecast_1 = models.PositiveIntegerField(
        verbose_name='Forecast for first team:'
    )
    forecast_2 = models.PositiveIntegerField(
        verbose_name='Forecast for second team:'
    )
    is_X2 = models.BooleanField(
        ("Is supermatch?"), default=False
    )

    class Meta:
        verbose_name = ("forecast")
        verbose_name_plural = ("forecasts")

    def __str__(self):
        return self.match


class Standing(TimeStampModel):

    title = models.CharField(
        verbose_name=('Title'), max_length=512, db_index=True
    )
    user = models.ForeignKey(
        'auth.User', related_name='standing',
        verbose_name=('user'), on_delete=models.CASCADE,
    )
    season = models.ForeignKey(
        'Season', related_name='standing',
        verbose_name=('season'), on_delete=models.CASCADE,
    )
    points = models.PositiveIntegerField(
        verbose_name='Total points'
    )

    class Meta:
        verbose_name = ("standing")
        verbose_name_plural = ("standings")

    def __str__(self):
        return self.title
