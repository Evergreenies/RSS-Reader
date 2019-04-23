from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from django.contrib import messages
import feedparser


class HomeView(TemplateView):
    """
        Basic template view
    """
    template_name = 'home.html'


class RSSRedirectView(RedirectView):
    """
        Handling 'post' request
    """

    def post(self, request, *args, **kwargs):
        """
        Handling 'post' request and return result
        :param request:
        :param args:
        :param kwargs:
        :return: feeds as list
        """

        url = self.request.POST.get('url', None)
        if url is not None and url is not '':
            feeds = feedparser.parse(url)
            feeds_list = feeds.entries

            if len(feeds_list) > 0:
                messages.info(request, f'Total {len(feeds_list)} feeds has been fetch.')
                return render(request, 'home.html', context={'feeds_list': feeds_list})
            else:
                messages.warning(request, 'Please, insert correct URL.')
                return render(request, 'home.html', context={'feeds_list': []})
        else:
            messages.warning(request, 'URL required.')
            return render(request, 'home.html', context={'feeds_list': []})
