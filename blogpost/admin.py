from django.contrib import admin
from .models import SampleModel, BlogModel

admin.site.register(BlogModel)
admin.site.register(SampleModel)
