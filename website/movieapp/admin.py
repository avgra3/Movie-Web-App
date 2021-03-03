from django.contrib import admin
from .models import Post, Director, Movie

# If you want to see the models on Admin website, add them below
admin.site.register(Post)
admin.site.register(Director)
admin.site.register(Movie)