from django.contrib import admin
from .models import Post, Directors, Movies

# If you want to see the models on Admin website, add them below
admin.site.register(Post)
admin.site.register(Directors)
admin.site.register(Movies)