"""NoteService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from NoteApp import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^logout/$', core_views.logout_user, name='logout'),
    url(r'^login/$', core_views.login_user, name='login'),
    url(r'^newNote/', core_views.newNote, name='AddNote'),
    url(r'^deleteNote/', core_views.deleteNote, name='DeleteNote'),
    url(r'^note/(?P<note_id>[0-9a-z-]+)', core_views.noteView, name='DeleteNote'),
    url(r'^$', core_views.home, name='home'),
]
