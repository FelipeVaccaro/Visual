from django.db import models

# Create your models here.
class categoria(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['nombre']
        indexes = [
            models.Intex(fields=['name']),
        ]
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    def __str__(self):
        return self.name