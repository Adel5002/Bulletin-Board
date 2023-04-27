from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import BoardListView, CreatePost, BoardDetailView, EditPost, DeletePost, AddComment

urlpatterns = [
    path('', BoardListView.as_view(), name='home'),
    path('add_post/', CreatePost.as_view(), name='add_post'),
    path('post/<slug:slug>/', BoardDetailView.as_view(), name='post_details'),
    path('post/<slug:slug>/edit/', EditPost.as_view(), name='edit_post'),
    path('post/<slug:slug>/delete/', DeletePost.as_view(), name='delete_post'),
    path('post/<slug:slug>/add_comment/', AddComment.as_view(), name='add_comment'),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)