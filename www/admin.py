from django.contrib import admin
from .models import Sensor, Alert, Data

admin.site.register(Sensor)
admin.site.register(Alert)
admin.site.register(Data)
