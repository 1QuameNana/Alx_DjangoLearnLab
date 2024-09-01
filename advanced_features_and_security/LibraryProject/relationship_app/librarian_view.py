from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def check_librarian(user):
    return user.userprofile.role == 'Librarians'

@user_passes_test(check_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/libray_detail.html')