from django.contrib import admin
from .models import Post,BlogMedia,BlogComment,Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(BlogMedia)
admin.site.register(BlogComment)
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    list_display= ('title','datetime_first','author','created_on','updated_on', 'updated_at')
