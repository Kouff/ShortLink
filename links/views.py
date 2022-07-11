from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, FormView
from django.views.generic.detail import SingleObjectMixin

from links.forms import LinkForm
from links.models import Link
from links.utils import create_short_link


class CreateShortLinkView(FormView):
    template_name = 'create_short_link.html'
    form_class = LinkForm

    def form_valid(self, form):
        link_obj = create_short_link(form.data['link'])
        return HttpResponseRedirect(reverse('detail_short_link', kwargs=dict(slug=link_obj.slug)))


class DetailShortLinkView(DetailView):
    template_name = 'detail_short_link.html'
    model = Link

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = context['object'].slug
        context['short_link'] = self.request.build_absolute_uri(f'/{slug}/')
        return context


class RedirectShortLinkView(SingleObjectMixin, View):
    model = Link

    def get(self, request, *args, **kwargs):
        link_obj = self.get_object()
        Link.objects.filter(id=link_obj.id).update(redirect_count=F('redirect_count') + 1)
        return HttpResponseRedirect(link_obj.link)
