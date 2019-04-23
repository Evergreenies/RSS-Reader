from django.urls import path
from reader_app.views import HomeView, RSSRedirectView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('rss-list', RSSRedirectView.as_view(), name='rss-list')
]
