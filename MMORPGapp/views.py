from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post


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

