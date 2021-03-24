from django import http
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin
from django_filters.views import FilterView
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from . import BlogSerializer, CommentSerializer
from .filters import Blogfilter
from .forms import BlogForm, BlogCommentForm
from ..models import Blog, BlogComment


def is_member(user):
    return user.groups.filter(name='일반').exists()


class BlogListViewSet(viewsets.ViewSet):
    queryset = Blog.objects.all()

    serializer_class = CommentSerializer

    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ('title',)


