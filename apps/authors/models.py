from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    biography = models.TextField(blank=True)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='authors/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name