"""
Django models for the Sticky Notes application.

This module defines the data models for creating and managing sticky notes
and their authors.
"""

from django.db import models


class StickyNote(models.Model):
    """
    Model representing a sticky note.
    
    A sticky note contains a title, content, timestamps for creation and updates,
    and an optional author reference.
    
    Attributes:
        title (str): The title of the sticky note (max 200 characters).
        content (str): The main content/body of the sticky note.
        created_at (datetime): Timestamp when the note was created.
        updated_at (datetime): Timestamp when the note was last updated.
        author (Author): Optional foreign key reference to the note's author.
    """
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """
        Return the string representation of the sticky note.
        
        Returns:
            str: The title of the sticky note.
        """
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Sticky Note"
        verbose_name_plural = "Sticky Notes"


class Author(models.Model):
    """
    Model representing an author of sticky notes.
    
    An author has a name and a unique email address.
    
    Attributes:
        name (str): The name of the author (max 100 characters).
        email (str): The unique email address of the author.
    """
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        """
        Return the string representation of the author.
        
        Returns:
            str: The name of the author.
        """
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = "Author"
        verbose_name_plural = "Authors"