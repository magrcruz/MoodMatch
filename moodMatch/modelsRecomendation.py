from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='static/img/genres', null=True, blank=True)
    
    TYPE_CHOICES = [
        ('film', 'Film'),
        ('song', 'Song'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    
    def __str__(self):
        return self.type+ ":"+ self.name

class Emotion(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Content(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    link = models.URLField()
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, null=True)
    
    TYPE_CHOICES = [
        ('movie', 'Movie'),
        ('song', 'Song'),
        ('serie','Serie')
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title