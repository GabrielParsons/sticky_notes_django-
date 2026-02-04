from django.shortcuts import render, get_object_or_404, redirect
from .models import StickyNote
from .forms import StickyNoteForm

# Create your views here.

def sticky_note_list(request):
    notes = StickyNote.objects.all()
    context = {"notes": notes,
               "page_title": "Sticky Notes"}
    return render(request, 'stickynotes/stickynotes_list.html', context)

def sticky_note_detail(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    return render(request, 'stickynotes/stickynotes_detail.html', {'note': note})

def sticky_note_create(request):
    if request.method == "POST":
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('sticky_note_detail', pk=note.pk)
    else:
        form = StickyNoteForm()
    return render(request, 'stickynotes/stickynotes_form.html', {'form': form})

def sticky_note_edit(request, pk):
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
    note = get_object_or_404(StickyNote, pk=pk)
    note.delete()
    return redirect('sticky_note_list')

