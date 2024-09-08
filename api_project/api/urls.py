from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet, basename='books' )

urlpatterns = [
    path('books/list/', BookViewSet.as_view({'get': 'list_books'}), name='list_books'),
    path('books/create', BookViewSet.as_view({'post': 'create_book'}), name='create_book'),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth')
    # path('', include(router.urls))
]

urlpatterns += router.urls