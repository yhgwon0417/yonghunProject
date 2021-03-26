from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Company, System, Inspection, Schedule, Blog, BlogType, Comment


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


admin.site.register(Blog)
admin.site.register(BlogType)
admin.site.register(Comment)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)


admin.site.register(Company)
admin.site.register(System)
admin.site.register(Inspection)
admin.site.register(Schedule)