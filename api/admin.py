from django.contrib import admin
from . import models

apiModels = [models.Movie, models.Rating]
admin.site.register(apiModels)
