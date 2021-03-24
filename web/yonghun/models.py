from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_pk = models.IntegerField(blank=True)
    email = models.EmailField(max_length=500, blank=True)
    nickname = models.CharField(max_length=200, blank=True)
    point = models.IntegerField(default=0)
    like = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, user_pk=instance.id)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='blog_create')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='blog_update')

    type = models.ForeignKey(BlogType, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=20, blank=False)
    content = RichTextUploadingField(blank=True, null=True, config_name='special',
                                     external_plugin_resources=[('youtube',
                                                                 '/static/ckeditor/plugins/youtube_2.1.14/youtube/',
                                                                 'plugin.js',
                                                                 )],
                                     )

    def get_absolute_url(self):
        return reverse('blog:blog-detail', args=[str(self.id)])


class BlogComment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='blog_comment_create')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='blog_comment_update')

    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='child_set')
    comment = models.CharField(max_length=20, blank=False)