from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.db import connection

# Creating the home page
def home(request):
    return render(request, 'movieapp/home.html')

# Movie Review Pages
class PostListView(ListView):
    model = Post
    template_name = 'movieapp/movie-reviews.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # Ordering output list
    ordering = ['-date_posted']
    # Number of reviews per page
    paginate_by = 5
    
# Movie Review Pages - Filtered by a user
class UserPostListView(ListView):
    model = Post
    template_name = 'movieapp/user-movie-reviews.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # Number of reviews per page
    paginate_by = 5
    # Limits our results to a specific user - if there is no username for them then we will get a 404 error
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

# Allow users to delete views
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    # When we delete - redirect back to the movie reviews page
    success_url = '/reviews/'
    
    # Verify that only users who wrote the post are able to delete their posts
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Login required mixin makes it so that if we try to make a post but are not logged in
# we are redirected to the login page
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    # Set author so that we can post without author errors
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Allows us to update our already created posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    # Set author so that we can post without author errors
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Verify that only users who wrote the post are able to edit their posts
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Creating the movies page
def movies(request):
    cursor = connection.cursor()
    mv = cursor.execute('''USE movies; SELECT * FROM directors;''')
    context = {'direct': mv}
    return render(request, 'movieapp/movies.html', context)

# Creating the directors page
def directors(request):
    return render(request, 'movieapp/directors.html')