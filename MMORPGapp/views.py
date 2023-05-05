from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .forms import PostForm, CommentForm
from .models import Post, Comment


class BoardListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'


class BoardDetailView(DetailView):
    model = Post
    template_name = 'postdetails.html'
    context_object_name = 'posts'


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)


class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'

    def get_queryset(self):
        self.post = get_object_or_404(Post, slug=self.kwargs['slug'])
        queryset = Post.objects.filter()
        return queryset


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'

    success_url = reverse_lazy('home')


class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment/add_comment.html'

    def form_valid(self, form):
        form.instance.post = Post.objects.get(slug=self.kwargs['slug'])
        comments = form.save(commit=False)
        comments.commentator = self.request.user
        comments.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_details', kwargs={'slug': self.object.post.slug})


class PrivateAccount(ListView):
    template_name = 'Responses_to_user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.filter(author=self.request.user)
        return queryset


class PrivAccPostResponses(DetailView):
    template_name = 'post_responses.html'
    context_object_name = 'posts'
    model = Post









