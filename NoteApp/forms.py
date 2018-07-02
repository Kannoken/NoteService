from django.forms import ModelForm
from NoteApp.models import Note, Category


class NewNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'category', 'mark', 'owner']



