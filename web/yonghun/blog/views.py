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
from rest_framework.generics import ListAPIView

from . import BlogSerializer
from .filters import Blogfilter
from .forms import BlogForm, BlogCommentForm
from ..models import Blog, BlogComment


def is_member(user):
    return user.groups.filter(name='일반').exists()


class BlogListView(LoginRequiredMixin, FilterView):
    filterset_class = Blogfilter
    template_name = 'blog/blog_list.html'  # your own name for the list as a template variable


class BlogListView2(ListAPIView):
    # filterset_class = Blogfilter
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # template_name = 'blog/blog_list2.html'  # your own name for the list as a template variable


class BlogDetailView(LoginRequiredMixin, FormMixin, generic.DetailView):
    model = Blog
    fields = ['name', ]
    template_name = 'blog/blog_detail.html'
    form_class = BlogCommentForm

    def get_success_url(self):  # post처리가 성공한뒤 행할 행동
        return reverse('blog:blog-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['comment_list'] = BlogComment.objects.filter(blog=self.kwargs['pk'], parent=None)
        context['form'] = BlogCommentForm(initial={'id':None, 'created_by': self.request.user, 'parent':None, 'blog':self.object.id })
        return context

    def post(self, request, *args, **kwargs):  # post요청이 들어왔을때.
        self.object = self.get_object()  # 현재페이지 object get.
        form = self.get_form()  # form데이터 받아오기

        if form.is_valid():  # form의 내용이 정상적일 경우
            return self.form_valid(form)  # form_valid함수 콜
        else:
            return self.form_invalid(form)

    def form_valid(self, form):  # form_valid함수
        comment = form.save(commit=False)  # form데이터를 저장. 그러나 쿼리실행은 x
        comment.blog = get_object_or_404(Blog, pk=self.object.pk)  # photo object를 call하여 photocomment의 photo로 설정(댓글이 속할 게시글 설정) pk로 pk설정 pk - photo id
        comment.id = form.id
        comment.created_by = self.request.user  # 댓글쓴 사람 설정.
        comment.save()  # 수정된 내용대로 저장. 쿼리실행

        return super(BlogDetailView, self).form_valid(form)


class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_create.html'
    success_url = '/yonghun/blog'


class BlogUpdateView(LoginRequiredMixin, generic.UpdateView):
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
