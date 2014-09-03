from blog.models import Blog, Post
from django.shortcuts import get_object_or_404, render


def blog_list(request):
    blogs = Blog.objects.all()
    submitters = []
    for blog in blogs:
        submitter = blog.submitter
        submitters.append(submitter)
    return render(request, "blog/blog_list.html", {
        "submitters": submitters,
        "blogs": blogs,
    })


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    likers = []
    comments = []
    for liker in blog.likers:
        likers.append(liker)
    for comment in blog.comments:
        comments.append(comment)
    return render(request, "blog/blog_detail.html", {
        "blog": submitters,
        "likers": likers,
        "comments": comments,
    })
