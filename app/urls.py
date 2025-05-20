from django.urls import path 
from . import views

urlpatterns = [
   # path('article/<int:pk>',views.detailBlog,name="Detail-Article"),
   path('',views.home, name = "All-blog"),
   # path('add/',views.addpost,name= 'Add-post'),
   # path('',views.blogEditor, name = "Add-Post")
]
