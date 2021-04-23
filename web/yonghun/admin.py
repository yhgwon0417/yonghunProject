from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Company, System, Inspection, Schedule, Blog, BlogType

admin.site.register(Blog)
admin.site.register(BlogType)

admin.site.register(User)
admin.site.register(Company)
admin.site.register(System)
admin.site.register(Inspection)
admin.site.register(Schedule)
