from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def check_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(check_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")