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

