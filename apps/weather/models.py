from django.db import models
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel


class WeatherForcast(TimeStampedModel):
    class SourceEnum(models.TextChoices):
        amindi = 'AMINDI.GE'
        openweather = 'OPENWEATHERMAP.ORG'

    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=64, verbose_name=_('location'))
    date = models.DateField(verbose_name=_('date'))
    time = models.TimeField(verbose_name=_('time'), null=True, blank=True)
    description = models.CharField(max_length=128, verbose_name=_('description'))
    temperature = models.FloatField(verbose_name=_('temperature'))
    temperature_feels_like = models.FloatField(verbose_name=_('feels like'), null=True)
    temperature_min = models.FloatField(verbose_name=_('min temperature'), null=True)
    temperature_max = models.FloatField(verbose_name=_('max temperature'), null=True)
    humidity = models.FloatField(verbose_name=_('humidity'), null=True)
    pressure = models.FloatField(verbose_name=_('pressure'), null=True)
    wind_speed = models.FloatField(verbose_name=_('wind speed'), null=True)
    wind_degree = models.FloatField(verbose_name=_('wind degree'), null=True)
    wind_gust = models.FloatField(verbose_name=_('wind gust'), null=True)
    visibility = models.IntegerField(verbose_name=_('visibility'), null=True)
    rain_probability = models.FloatField(verbose_name=_('rain probability'), null=True)
    source = models.CharField(max_length=32, verbose_name=_('source of information'))

    def __str__(self):
        return f'{self.location}({self.date} {self.time})'
