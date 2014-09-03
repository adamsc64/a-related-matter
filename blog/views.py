from blog.models import Blog, Post
from django.shortcuts import get_object_or_404, render


def blog_list(request):
    blogs = Blog.objects.all()
    if request.GET.get("optimized") == "true":
        blogs = blogs.select_related("submitter")
        blogs = blogs.prefetch_related("posts", "posts__likers")
    datasets = []
    for blog in blogs:
        submitter = blog.submitter
        posts = list(blog.posts.all())
        datasets.append({"blog": blog,
                         "submitter": submitter,
                         "posts": posts,
                         })
    return render(request, "blog/blog_list.html", {
        "datasets": datasets,
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
        "blog": blog,
        "likers": likers,
        "comments": comments,
    })
