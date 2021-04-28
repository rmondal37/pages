from django.contrib import admin
from .models import WebPage, Topic, AccessRecord

# Register your models here.

admin.site.register(WebPage)
admin.site.register(Topic)
admin.site.register(AccessRecord)