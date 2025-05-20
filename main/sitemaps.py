from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from app.models import Post

class StaticViewSitemap(Sitemap):
    priority = 1
    changefreq = 'daily'

    def items(self):
        return [
            'home',
            'document_translation',
            'refund_policy',
            'privacy_policy',
            'terms_and_conditions',
            'edu',
            'e_commerce',
            'banking',
            'government',
            'demo_msg_save',
            'All-blog',
        ]

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return reverse('Detail-Article', args=[obj.pk])

