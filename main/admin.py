from django.contrib import admin
from .models import Season, Stage, Match, Forecast, Standing

# Register your models here.


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug'
    )
    list_filter = ('is_published',)
    search_fields = ['title']
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug', 'season'
    )
    list_filter = ('is_published',)
    search_fields = ['title', 'season']
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug', 'result_1', 'result_2', 'stage'
    )
    list_filter = ('is_published',)
    search_fields = ['title', 'stage']
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = (
        'match', 'forecast_1', 'forecast_2', 'is_X2'
    )
    list_filter = ('is_published',)
    search_fields = ['match']
    ordering = ('match',)


@admin.register(Standing)
class StandingAdmin(admin.ModelAdmin):
    list_display = (
        'season', 'points'
    )
    list_filter = ('is_published',)
    search_fields = ['season']
    ordering = ('season',)
