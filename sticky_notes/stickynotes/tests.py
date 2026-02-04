from django.test import TestCase
from django.urls import reverse
from .models import StickyNote, Author

# Create your tests here.

class StickyNoteTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.sticky_note = StickyNote.objects.create(
            title="Test Note",
            content="This is a test sticky note.",
            author=self.author
        )

    def test_sticky_note_creation(self):
        self.assertEqual(self.sticky_note.title, "Test Note")
        self.assertEqual(self.sticky_note.content, "This is a test sticky note.")
        self.assertEqual(self.sticky_note.author.name, "Test Author")

    def test_sticky_note_list_view(self):
        response = self.client.get(reverse('sticky_notes:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_sticky_note_detail_view(self):
        response = self.client.get(reverse('sticky_notes:detail', args=[self.sticky_note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is a test sticky note.")

    def test_sticky_note_update_view(self):
        response = self.client.post(reverse('sticky_notes:update', args=[self.sticky_note.id]), {
            'title': "Updated Test Note",
            'content': "This is an updated test sticky note.",
            'author': self.author.id
        })
        self.assertEqual(response.status_code, 302)  # Redirect after update
        self.sticky_note.refresh_from_db()
        self.assertEqual(self.sticky_note.title, "Updated Test Note")
        self.assertEqual(self.sticky_note.content, "This is an updated test sticky note.")  

    