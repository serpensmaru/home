from django.contrib import admin
from .models import Sensor, Measurement


@admin.register(Sensor)
class Sensor_admin(admin.ModelAdmin):
    list_display = ["name", "description"]


@admin.register(Measurement)
class Measurement_admin(admin.ModelAdmin):
    list_display = ["sensor", "temperature", "created_at"]
