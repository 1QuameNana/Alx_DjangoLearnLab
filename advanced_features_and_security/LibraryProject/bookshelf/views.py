from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from .forms import ExampleForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get("role")
            if role == "creator":
                creator_group = Group.objects.get(name="Creator")
                user.groups.add(creator_group)
            elif role == "reader":
                creator_group = Group.objects.get(name="Reader")
                user.groups.add(creator_group)
            
            login(request, user)
            return redirect("list_posts")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

def book_list(request):
    books = Book.objects.all()
    return render(request, "blog/book_list.html", {"post": books})

@login_required
@permission_required("blog.create", raise_exception=True)
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.author = request.user
            posts.save()
            return redirect("list_posts")
        
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form})
# Create your views here.
