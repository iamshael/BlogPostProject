from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from .models import Post


def home(request):

    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogapp/home.html', context)


def about(request):
    return render(request, 'blogapp/about.html', {'title': 'About'})


class PostListView(ListView): #used instead of home view #Using our conventions
    model = Post
    template_name = 'blogapp/home.html' # default=> <app>/<model>_viewtype<>/
    context_object_name = 'posts' #otherwise default is post_list will be searcched
    ordering= ['-date_posted'] # for odering latest posts to appear first
    paginate_by = 5

class UserPostListView(ListView): #used instead of home view #Using our conventions
    model = Post
    template_name = 'blogapp/user_post.html' # default=> <app>/<model>_viewtype<>/
    context_object_name = 'posts' #otherwise default is post_list will be searcched
    # ordering= ['-date_posted'] # for odering latest posts to appear first
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')


class PostDetailView(DetailView): #Used default convention of django to save lines of code
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView): #Used default convention of django to save lines of code
    model = Post
    fields =['title', 'content'] # forms fields. We dont need to create form object in CBV Directly pass in template

    def form_valid(self, form): #Overriden for adding current user as author
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #Same as CreateView No need to create Template Django will handle
    model = Post
    fields =['title', 'content']
# this view default uses post_form template.. so need to create template for update
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
#current login user should not able to update post of other users
    def test_func(self):
        post = self.get_object() #getting current Post

        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #same as DetailView
    model = Post
    success_url = '/' #to redirect to home after delete the post

    def test_func(self):
        post = self.get_object() #getting current Post

        if self.request.user == post.author:
            return True
        return False
