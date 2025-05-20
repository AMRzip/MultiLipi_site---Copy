from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView, CreateView
from .models import Post, BlogComment
from . import forms
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
 
def home(request):
    # post_list = Post.objects.filter(is_draft=False)
    # paginator = Paginator(post_list, 8)
    # page = request.GET.get('page', 1)

    # try:
    #     posts = paginator.page(page)
    # except PageNotAnInteger:
    #     posts = paginator.page(1)
    # except EmptyPage:
    #     posts = paginator.page(paginator.num_pages)

    # context = {"posts": posts}
    return render(request, 'app/allblog.html')


def detailBlog(request,pk):
    # print('detail me aaya')
    post = Post.objects.get(pk=pk)  
    if request.method == 'POST':
        # print('detail ke comment')
        name= request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        blogobj, created = BlogComment.objects.get_or_create(name=name,email=email,comment=comment,blog=post) 

    return render(request,'app/detailarticle.html')  


        

# class DetailArticle(DetailView):
#     model= Post 
#     template_name = "detailarticle.html"


    
            

# def addpost(request):

#     form = forms.Blogform()
#     print(form)
#     if request.method == 'POST':
#         form = forms.Blogform(request.POST)
#         if(form.is_valid):
#             form.save() 
#             form = forms.Blogform
#     context = {"form":form} 
#     return render(request,'add_post.html',context)       


    



