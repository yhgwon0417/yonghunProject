from importlib._common import _

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.urls import reverse

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractUser, UserManager

from django.utils import timezone


class UserManager(UserManager):
    def create_superuser(self, *args, **kwargs):
        return super().create_superuser(*args, **kwargs)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    objects = UserManager()  # blank=True: 폼(입력양식)에서 빈채로 저장되는 것을 허용, DB에는 ''로 저장 # CharField 및 TextField는 blank=True만 허용, null=True 허용 X n
    nickname = models.CharField(blank=True, max_length=50)
    introduction = models.TextField(blank=True, max_length=200)
    # profile_image = models.ImageField(blank=True, null=True)  # null=True: DB에 NULL로 저장

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]


class Company(models.Model):
    name = models.CharField(max_length=20, blank=False)
    team = models.CharField(max_length=20, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class System(models.Model):
    type = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.type


class Schedule(models.Model):
    # class Meta:
    #     ordering = ['start_date']
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=False)
    institution = models.CharField(max_length=100, blank=False, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    detail = models.CharField(max_length=100, blank=False, null=True)

    def __str__(self):
        return f'[{self.start_date}~{self.end_date}] {self.institution}'


class Inspection(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL, null=True, blank=False)
    system = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=False)
    count = models.IntegerField()

    def __str__(self):
        return f'[{self.schedule.start_date}~{self.schedule.end_date}] {self.schedule.institution} / {self.system}({self.count})'


class BlogType(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name


class Blog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='blog_update')

    type = models.ForeignKey(BlogType, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=20, blank=False)
    content = models.TextField(max_length=1000000)

    def get_absolute_url(self):
        return reverse('blog:blog-detail', args=[str(self.id)])
