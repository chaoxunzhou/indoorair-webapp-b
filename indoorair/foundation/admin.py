from django.contrib import admin

from .models import Instrument, Sensor, TimeSeriesDatum


admin.site.register(Instrument)
admin.site.register(Sensor)
admin.site.register(TimeSeriesDatum)
