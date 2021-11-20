from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.text import slugify


class PageData(models.Model):  # pylint: disable=too-many-instance-attributes
    """Prototype pages for Clients"""

    client_code = models.CharField(max_length=60, null=False)
    title = models.CharField(max_length=400, null=False)
    display = models.BooleanField(default=True)
    date_added = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(
        default='', editable=False, max_length=60, null=False)

    def get_absolute_url(self):
        """Adds slug to url for page redirection."""
        kwargs = {'slug': self.slug,
                  'pk': self.id
                  }
        return reverse('info:page-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        """Creates and adds url slug.
        Resizes and saves images."""
        slug_value = self.title
        self.slug_en = slugify(slug_value, allow_unicode=True)

        super().save(*args, **kwargs)

    class Meta:
        """Orders by the most recent created by default."""
        ordering = ['date_added']

    def __str__(self):
        return f'{self.client_code}'
