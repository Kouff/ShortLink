import random
import string
from django.db import IntegrityError

from links.models import Link

symbols = string.ascii_letters + string.digits


def generate_slug(n: int) -> str:
    return ''.join(random.choice(symbols) for _ in range(n))


def create_short_link(link: str) -> Link:
    used_slugs = Link.objects.values_list('slug')
    while True:
        slug = generate_slug(7)
        if slug in used_slugs:
            continue
        try:
            return Link.objects.create(link=link, slug=slug)
        except IntegrityError:
            pass
