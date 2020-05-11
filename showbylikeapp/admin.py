from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Posts)
admin.site.register(Images)
admin.site.register(Tags)
admin.site.register(Likes)