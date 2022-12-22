from django.contrib import admin
from .models import *

# Register your models here.

class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Food)
admin.site.register(Feedback)
admin.site.register(Cookers)