from django.shortcuts import render

# Creating the home page
def home(request):
    return render(request, 'movieapp/home.html')

# Creating the movies page
def movies(request):
    return render(request, 'movieapp/movies.html')

# Creating the directors page
def directors(request):
    return render(request, 'movieapp/directors.html')