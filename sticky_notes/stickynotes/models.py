from django.db import models

# Create your models here.
#include fields for title and content of each sticky note

class StickyNote(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Sticky Note"
        verbose_name_plural = "Sticky Notes"

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = "Author"
        verbose_name_plural = "Authors"