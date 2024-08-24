from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from .views import list_books, LibraryDetailView, index, add_book, change_book, delete_book
from . import views
from .views import librarian_view, member_view
#from admin_view import admin_view


urlpatterns = [
    path('books/', list_books, name='list_all_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_books'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('', index, name='index'),
    path('accounts/profile/', TemplateView.as_view(template_name='relationship_app/profile.html'), name='profile'),

    #path('admin/', admin_view, name='admin_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),

    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', change_book, name='change_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
]