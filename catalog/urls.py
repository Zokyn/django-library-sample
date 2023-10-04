from django.urls import path
from . import views 
# static imports 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book_details'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
