from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class City(models.Model):

    name = models.CharField(_("Name"), max_length=100) # name in CSV file
    symbol = models.CharField(_("Symbol"), max_length=2) # admin1 in CSV file
    country = models.CharField(_("Country"), max_length=2) # country in CSV file
    latitude = models.FloatField(_("Latitude")) # lat in CSV file
    longitude = models.FloatField(_("Longitude")) # long in CSV file
    population = models.IntegerField(_("Poplation")) # population in CSV file
    timeZone = models.CharField(_("Time Zone"), max_length=32) # tz in CSV file

    class Meta:
        app_label = 'cities'
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return self.name

