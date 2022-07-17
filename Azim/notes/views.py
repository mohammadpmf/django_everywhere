from django.shortcuts import render
# from django.http import HttpResponse
from .models import Note

# def show_test(request):
#     return HttpResponse("Test Notes")

def notes_list_view(request):
    notes = Note.objects.all()
    context = {
        'notes': notes,
    }
    return render(request, "notes/notes_list.html", context)
