from blog.models import Blog, Post
from django.shortcuts import get_object_or_404, render


def blog_list(request):
    blogs = Blog.objects.all()
    if request.GET.get("optimized") == "true":
        blogs = blogs.select_related("submitter")
    return render(request, "blog/blog_list.html", {
        "blogs": blogs,
    })


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    posts = Post.objects.filter(blog=blog)
    if request.GET.get("optimized") == "true":
        posts = posts.prefetch_related("comments__submitter", "likers")
    return render(request, "blog/blog_detail.html", {
        "blog": blog,
        "posts": posts,
    })
