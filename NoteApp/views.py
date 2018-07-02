from django.shortcuts import render

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from NoteApp.models import Note, Category
from NoteApp.forms import NewNoteForm
from django.views.decorators.csrf import csrf_exempt
from django.forms import HiddenInput


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        log = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        log = AuthenticationForm()
    return render(request, 'signup.html', {'form1': form, 'form': log})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'signup.html')


def home(request):
    notes = {}
    form = NewNoteForm()
    category = Category.objects.all()

    if request.user.is_authenticated:
        notes = Note.objects.filter(owner=request.user.id)
    return render(request, 'index.html', {'notes': notes, 'form': form, 'category': category})


def newNote(request):
    if request.method == 'POST':

        user = request.user
        post_values = request.POST.copy()

        post_values['owner'] = user.id
        form = NewNoteForm(post_values)
        # Check if the form is valid:
        if form.is_valid():
            form.save()
    return render(request, 'index.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')


@csrf_exempt
def deleteNote(request):
    if request.method == 'POST':
        note = Note.objects.get(id=request.POST['id'])
        note.delete()
    return render(request, 'index.html')


@csrf_exempt
def noteView(request, note_id):
    note = Note.objects.get(id=note_id)
    form = NewNoteForm(instance=note)
    form.fields['owner'].widget = HiddenInput()
    if request.method == 'POST':
        form = NewNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
    category = Category.objects.all()
    return render(request, 'note.html', {'form': form, 'category': category})

# Create your views here.
