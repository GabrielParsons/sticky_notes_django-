"""
Django views for the Sticky Notes application.

This module contains view functions for creating, reading, updating,
and deleting (CRUD) sticky notes.
"""

from django.shortcuts import render, get_object_or_404, redirect
from .models import StickyNote
from .forms import StickyNoteForm


def sticky_note_list(request):
    """
    Display a list of all sticky notes.
    
    Args:
        request: The HTTP request object.
        
    Returns:
        HttpResponse: Rendered template with list of all sticky notes.
    """
    notes = StickyNote.objects.all()
    context = {"notes": notes,
               "page_title": "Sticky Notes"}
    return render(request, 'stickynotes/stickynotes_list.html', context)


def sticky_note_detail(request, pk):
    """
    Display details of a specific sticky note.
    
    Args:
        request: The HTTP request object.
        pk (int): Primary key of the sticky note to display.
        
    Returns:
        HttpResponse: Rendered template with sticky note details.
        
    Raises:
        Http404: If the sticky note with the given pk does not exist.
    """
    note = get_object_or_404(StickyNote, pk=pk)
    return render(request, 'stickynotes/stickynotes_detail.html', {'note': note})


def sticky_note_create(request):
    """
    Create a new sticky note.
    
    Handles both GET (display form) and POST (process form) requests.
    
    Args:
        request: The HTTP request object.
        
    Returns:
        HttpResponse: On GET, renders form template. On successful POST,
                     redirects to the detail view of the newly created note.
    """
    if request.method == "POST":
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('sticky_note_detail', pk=note.pk)
    else:
        form = StickyNoteForm()
    return render(request, 'stickynotes/stickynotes_form.html', {'form': form})


def sticky_note_edit(request, pk):
    """
    Edit an existing sticky note.
    
    Handles both GET (display form) and POST (process form) requests.
    
    Args:
        request: The HTTP request object.
        pk (int): Primary key of the sticky note to edit.
        
    Returns:
        HttpResponse: On GET, renders form template with current note data.
                     On successful POST, redirects to the detail view of the updated note.
                     
    Raises:
        Http404: If the sticky note with the given pk does not exist.
    """
    note = get_object_or_404(StickyNote, pk=pk)
    if request.method == "POST":
        form = StickyNoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            return redirect('sticky_note_detail', pk=note.pk)
    else:
        form = StickyNoteForm(instance=note)
    return render(request, 'stickynotes/stickynotes_form.html', {'form': form})


def sticky_note_delete(request, pk):
    """
    Delete an existing sticky note.
    
    Args:
        request: The HTTP request object.
        pk (int): Primary key of the sticky note to delete.
        
    Returns:
        HttpResponse: Redirects to the list view after successful deletion.
        
    Raises:
        Http404: If the sticky note with the given pk does not exist.
    """
    note = get_object_or_404(StickyNote, pk=pk)
    note.delete()
    return redirect('sticky_note_list')

