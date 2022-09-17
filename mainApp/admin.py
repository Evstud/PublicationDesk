from django.contrib import admin
from .models import Notice, Response, OneTimeCode

admin.site.register(Notice)
admin.site.register(Response)
admin.site.register(OneTimeCode)

