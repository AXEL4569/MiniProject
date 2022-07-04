from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Profile)
admin.site.register(models.Gigs)
admin.site.register(models.Reviews)