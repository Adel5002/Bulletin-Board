from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import BoardListView, CreatePost, BoardDetailView

urlpatterns = [
    path('', BoardListView.as_view(), name='home'),
    path('add_post/', CreatePost.as_view(), name='add_post'),
    path('post/<slug:slug>/', BoardDetailView.as_view(), name='post_details'),

]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)