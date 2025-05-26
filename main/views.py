from django.shortcuts import render, redirect
from .models import *
from app.models import *
from .forms import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string
import os

CURR = os.getenv('CURR','USD')

# Create your views here.
def index(request):
    posts = Post.objects.filter(is_draft=False)
    # context = {"posts":posts} 
    return render(request, "main/home.html")

@csrf_exempt
def demo_msg_save(request):
    if request.method == "POST":
        body = json.loads(request.body)
        try:
            Request_a_Demo.objects.create(
                site_name= body["site_name"],
                full_name = body["full_name"],
                email = body["email"],
                phone_no = body["phone_no"],
                company_name = body["company_name"],
                subject = body["subject"],
                message = body["message"],
            ).save()
        except:
            pass
    return HttpResponse(status=200)

def document_trans(request):
    posts = Post.objects.filter(is_draft=False)
    langs = ['Assamese',
            'Bengali',
            'Bodo',
            'Dogri',
            'Goan Konkani',
            'Gujarati',
            'Hindi',
            'Kannada',
            'Kashmiri',
            'Maithili',
            'Malayalam',
            'Marathi',
            'Manipuri',
            'Nepali',
            'Odia',
            'Punjabi',
            'Sanskrit',
            'Santali',
            'Sindhi',
            'Tamil',
            'Telugu',
            'Urdu']
    lang_dict = {
        "Korean": 0.3,
        'Vietnamese': 0.25,
        'Mandarin Chinese': 0.3,
        'Spanish': 0.25,
        'French': 0.25,
        'Arabic': 0.3,
        'Russian': 0.3,
        'Portuguese': 0.25,
        'Urdu': 0.2,
        'Indonesian': 0.20,
        'Japanese': 0.35,
        'German': 0.3
    }
    return render(request, "main/doc_trans.html")

def contact_us(request):
    return render(request, "main/contact_us.html")

def seo(request):
    # posts = Post.objects.filter(is_draft=False)
    return render(request, "main/seo.html")

def temp(request):
    return render(request, "main/temp.html")

def home(request):
    return render(request, "main/home.html")

def pricing(request):
    return render(request, "main/pricing.html",{'curr': CURR})

def edu(request):
    return render(request, "main/edu.html")

# def e_commerce(request):
#     return render(request, "main/e_commerce.html")

# def banking(request):
#     return render(request, "main/banking.html")

# def government(request):
#     return render(request, "main/government.html")

def refund_policy(request):
    return render(request, "main/refund_policy.html")

def privacy_policy(request):
    return render(request, "main/privacy_policy.html")

def terms_and_conditions(request):
    return render(request, "main/terms_and_conditions.html")

def robots_txt(request):
    sitemap_url = request.build_absolute_uri(reverse('django.contrib.sitemaps.views.sitemap'))
    content = render_to_string('robots.txt', {'sitemap_url': sitemap_url})
    return HttpResponse(content, content_type='text/plain')

def custom_404_view(request, exception):
    return redirect('/')

def wordpress(request):
    # posts = Post.objects.filter(is_draft=False)
    # context = {"posts":posts} 
    return render(request, "integrations/integration-wordpress.html")

def wix(request):
    # posts = Post.objects.filter(is_draft=False)
    # context = {"posts":posts} 
    return render(request, "integrations/integration-wix.html")

def shopify(request):
    # posts = Post.objects.filter(is_draft=False)
    # context = {"posts":posts} 
    return render(request, "integrations/integration-shopify.html")

def webflow(request):
    # posts = Post.objects.filter(is_draft=False)
    # context = {"posts":posts} 
    return render(request, "integrations/integration-webflow.html")

def ecommerce(request):
    # posts = Post.objects.filter(is_draft=False)
    # context = {"posts":posts} 
    return render(request, "solutions/solution-ecommerce.html")

def goverment(request):
    # posts = Post.objects.filter(is_draft=False)
    # context = {"posts":posts}
    return render(request, "solutions/solution-goverment.html")

def marketing(request):
    # posts = Post.objects.filter(is_draft=False)
    # context = {"posts":posts}
    return render(request, "solutions/solution-marketing.html")

def web_agency(request):
    # posts = Post.objects.filter(is_draft=False)
    # context = {"posts":posts}
    return render(request, "solutions/solution-web-agency.html")

def referral(request):
    # posts = Post.objects.filter(is_draft=False)
    # context = {"posts":posts}
    return render(request, "main/referral.html")

def wordcount(request):
    return render(request, "main/wordcount-url.html")

def wordcount_analytics(request):
    return render(request, "main/wordcount-main.html")

def avilable_langs(request):
    return render(request, "main/avilable_langs.html")