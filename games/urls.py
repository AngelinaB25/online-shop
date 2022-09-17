from django.urls import path
from games.views import home
from django.conf import settings
from django.conf.urls.static import static
from games.views import GameListView,GameDetailView
urlpatterns = [
    path('',GameListView.as_view(),name='home'),
    path('<slug:slug>/',GameDetailView.as_view(),name = 'game_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)