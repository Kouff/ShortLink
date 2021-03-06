from django.urls import path

from links.views import CreateShortLinkView, DetailShortLinkView, RedirectShortLinkView

urlpatterns = (
    path('', CreateShortLinkView.as_view(), name='create_short_link'),
    path('<slug:slug>/detail/', DetailShortLinkView.as_view(), name='detail_short_link'),
    path('<slug:slug>/', RedirectShortLinkView.as_view(), name='redirect_short_link'),
)
