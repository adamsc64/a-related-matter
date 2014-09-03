text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
        "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut "
        "enim ad minim veniam, quis nostrud exercitation ullamco laboris "
        "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
        "reprehenderit in voluptate velit esse cillum dolore eu fugiat "
        "nulla pariatur. Excepteur sint occaecat cupidatat non proident, "
        "sunt in culpa qui officia deserunt mollit anim id est laborum."
        )


def create_sample(num_users=20,
                  num_blogs=50,
                  num_posts_per_blog=4,
                  num_comments_per_post=7,
                  ):
    for i in range(0, num_users):
        User.objects.create_user('u%s' % i, 'u%s@test.com' % i, '')
    users = list(User.objects.all())
    for i in range(0, num_blogs):
        blog.submitter = random.choice(users)
        blog.name = random.choice(text.split())
        blog.save()
    for blog in Blog.objects.all():
        blog.submitter = random.choice(users)
        blog.save()
        for i in range(0, num_posts_per_blog)
        post = Post.objects.create(body=text, blog=blog)
        for u in User.objects.all():
            post.likers.add(u)
    for post in Post.objects.all():
        post.name = random.choice(text.split())
        post.save()
        for i in range(0, num_comments_per_post):
            PostComment.objects.create(submitter=random.choice(users)),
                                       post=post,
                                       body=text,
                                       )
