from django.contrib import admin
from blog.models import Blog, Post, PostComment


admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(PostComment)
