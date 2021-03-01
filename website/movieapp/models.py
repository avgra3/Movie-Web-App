from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # helps Django get the url to reroute the user after creating a post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Directors(models.Model):
    director_id = models.AutoField(primary_key=True)
    director_first_name = models.CharField(max_length=40)
    director_last_name = models.CharField(max_length=40)
    director_dob = models.DateField(blank=True, null=True)
    director_country = models.CharField(max_length=3)

    class Meta:
        managed = True
        db_table = 'directors'

    def __str__(self):
        return (self.director_first_name + " " + self.director_last_name)


class Movies(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=100)
    movie_release_year = models.TextField()  # This field type is a guess.
    movie_format = models.CharField(max_length=20)
    movie_genre = models.CharField(max_length=20)
    movie_want = models.CharField(max_length=2)
    movie_own = models.CharField(max_length=2)
    director_Name = models.ForeignKey(Directors, models.DO_NOTHING, db_column='director_id_1', null=False, related_name='director_id_1')
    director_Name_2 = models.ForeignKey(Directors, models.DO_NOTHING, db_column='director_id_2', null=True, blank=True, related_name='director_id_2')

    class Meta:
        managed = False
        db_table = 'movies'

    def __str__(self):
        return (self.movie_name)