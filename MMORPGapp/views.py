from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

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


