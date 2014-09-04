import random
from blog.models import Blog, Post, PostComment
from django.contrib.auth.models import User


text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
        "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut "
        "enim ad minim veniam, quis nostrud exercitation ullamco laboris "
        "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
        "reprehenderit in voluptate velit esse cillum dolore eu fugiat "
        "nulla pariatur. Excepteur sint occaecat cupidatat non proident, "
        "sunt in culpa qui officia deserunt mollit anim id est laborum."
        )
names = ["Jack", "William", "Emma", "Olivia", "Emily", "Sophia", "Ava",
         "Lily", "Ella", "Isabella", "Noah", "Ethan", "Oliver", "Thomas",
         "Cooper", "James", "Lucas", "Lachlan",
         ]

def create_sample(num_blogs=50,
                  num_posts_per_blog=4,
                  num_comments_per_post=7,
                  ):
    for name in names:
        User.objects.create_user(name, '%s@test.com' % name, '')
    users = list(User.objects.all())
    for i in range(0, num_blogs):
        blog = Blog()
        blog.submitter = random.choice(users)
        blog.name = random.choice(text.split())
        blog.save()
    for blog in Blog.objects.all():
        blog.submitter = random.choice(users)
        blog.save()
        for i in range(0, num_posts_per_blog):
            post = Post.objects.create(body=text,
                                       blog=blog,
                                       name=random.choice(text.split()),
                                       )
            for u in users:
                if random.choice(range(0, 6)) == 0:
                    post.likers.add(u)
    for post in Post.objects.all():
        for i in range(0, num_comments_per_post):
            PostComment.objects.create(submitter=random.choice(users),
                                       post=post,
                                       body=text,
                                       )
