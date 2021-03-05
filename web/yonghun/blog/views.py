from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import request
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin
from django_filters.views import FilterView
from requests import post
from rest_framework.generics import ListAPIView

from . import BlogSerializer
from .filters import Blogfilter
from .forms import BlogForm, BlogCommentForm
from ..models import Blog, BlogComment


class BlogListView(FilterView):
    filterset_class = Blogfilter
    template_name = 'blog/blog_list.html'  # your own name for the list as a template variable


class BlogDetailView(FormMixin, generic.DetailView):
    model = Blog

    template_name = 'blog/blog_detail.html'
    form_class = BlogCommentForm

    def get_success_url(self):  # post처리가 성공한뒤 행할 행동
        return reverse('blog:blog-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['comment_list'] = BlogComment.objects.filter(blog=self.kwargs['pk'], parent=None)

        context['form'] = BlogCommentForm(initial={'user': self.request.user, 'blog': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(BlogDetailView, self).form_valid(form)


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


class BlogCommentCreateView(generic.CreateView):
    model = BlogComment
    form_class = BlogCommentForm

    template_name = 'blog/blogcomment_create.html'
    success_url = '/yonghun/blog'

# class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
#     def test_func(self):
#         return self.request.user.groups.filter(name="공통").exists()
#
#     model = Blog
#     template_name = 'molit/blog/blog_confirm_delete.html'
#     success_url = '/molit/blog'
