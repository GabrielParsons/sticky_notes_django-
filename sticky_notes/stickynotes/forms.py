"""
Django forms for the Sticky Notes application.

This module defines form classes for creating and editing sticky notes
through the web interface.
"""

from django import forms 
from .models import StickyNote


class StickyNoteForm(forms.ModelForm):
    """
    Form for creating and editing sticky notes.
    
    This ModelForm provides a user-friendly interface for managing sticky notes
    with custom widget styling applied to all fields.
    
    Meta:
        model: StickyNote model that this form is based on.
        fields: List of fields to include in the form (title, content, author).
        widgets: Custom widget configurations with CSS classes for styling.
    """
    
    class Meta:
        model = StickyNote
        fields = ['title', 'content', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }