from django.shortcuts import render

# Creating the home page
posts = [
        {'author': 'Test',
        'title': 'Entry 1',
        'content': 'Post entry 1',
        'date_posted': 'February 10, 2021'},
        {'author': 'Test',
        'title': 'Entry 1',
        'content': 'Post entry 2',
        'date_posted': 'February 10, 2030'},
        {'author': 'Test',
        'title': 'Entry 3',
        'content': 'Post entry 3',
        'date_posted': 'February 11, 2030'}
        ]


def home(request):
    return render(request, 'movieapp/home.html')

# Creating the movies page
def movies(request):
    return render(request, 'movieapp/movies.html')

# Creating the directors page
def directors(request):
    return render(request, 'movieapp/directors.html')

# Creating the movie reviews page
def reviews(request):
    context = {'posts': posts}
    return render(request, 'movieapp/movie-reviews.html', context)