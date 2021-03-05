from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import request
from django.shortcuts import render
from django.views import generic
from django_filters.views import FilterView
from rest_framework.generics import ListAPIView

from . import BlogSerializer
from .filters import Blogfilter
from .forms import BlogForm
from ..models import Blog


class BlogListView(FilterView):
    filterset_class = Blogfilter
    template_name = 'blog/blog_list.html'  # your own name for the list as a template variable


class BlogListView2(ListAPIView):
    # filterset_class = Blogfilter
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # template_name = 'blog/blog_list2.html'  # your own name for the list as a template variable


class BlogDetailView(generic.DetailView):
    model = Blog
    fields = ['name', ]
    template_name = 'blog/blog_detail.html'


class BlogCreateView(generic.CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_create.html'
    success_url = '/yonghun/blog'


class BlogUpdateView(generic.UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_update_form.html'
    success_url = '/yonghun/blog'


class BlogDeleteView(generic.DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = '/yonghun/blog'

# class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
#     def test_func(self):
#         return self.request.user.groups.filter(name="공통").exists()
#
#     model = Blog
#     template_name = 'molit/blog/blog_confirm_delete.html'
#     success_url = '/molit/blog'
