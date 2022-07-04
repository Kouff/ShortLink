from django.test import TestCase, Client
from django.urls import reverse

from links.models import Link


class LinkTestCase(TestCase):
    def setUp(self):
        pass

    def test_link(self):
        c = Client()

        c.post(reverse('create_short_link'), dict(link='test'))
        self.assertEqual(Link.objects.count(), 0)

        c.post(reverse('create_short_link'), dict(link='https://docs.djangoproject.com/'))
        self.assertEqual(Link.objects.count(), 1)

        link = Link.objects.get()

        response = c.get(reverse('redirect_short_link', kwargs=dict(slug=link.slug)))
        self.assertEqual(link.redirect_count, 0)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], link.link)
        link.refresh_from_db()
        self.assertEqual(link.redirect_count, 1)
