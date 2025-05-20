from django.urls import path
from . import views
from .sitemaps import StaticViewSitemap, BlogSitemap
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap
}

urlpatterns = [
    path("", views.index, name='home'),
    path("Document Translation", views.document_trans, name='document_translation'),
    path("Multilingual SEO", views.seo, name='seo'),

    path("refund_policy", views.refund_policy, name="refund_policy"),
    path("privacy_policy", views.privacy_policy, name="privacy_policy"),
    path("terms_and_conditions", views.terms_and_conditions, name="terms_and_conditions"),

    # path("edu", views.edu, name="edu"),
    # path("E_commerce", views.e_commerce, name="e_commerce"),
    # path("banking", views.banking, name="banking"),
    # path("government", views.government, name="government"),

    path("pricing", views.pricing, name="pricing"),
    path("referral", views.referral, name="referral"),

    path('wordcount', views.wordcount, name='wordcount'),
    path('wordcount_analytics', views.wordcount_analytics, name='wordcount_analytics'),

    path("contact_us", views.contact_us),
    path("demo_msg_save", views.demo_msg_save, name="demo_msg_save"),

    path("temp", views.temp),
    path('wordpress', views.wordpress, name="wordpress"),
    path('wix', views.wix, name="wix"),
    path('shopify', views.shopify, name="shopify"),
    path('webflow', views.webflow, name="webflow"),

    path('ecommerce', views.ecommerce, name="ecommerce"),
    path('goverment', views.goverment, name="government"),
    path('marketing', views.marketing, name="marketing"),
    path('webagency', views.web_agency, name="web_agency"),

    # path("home", views.home),
    
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
]