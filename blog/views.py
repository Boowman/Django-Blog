from django.shortcuts import render, render_to_response
from django.utils import timezone
from blog.models import Post, Comment


def viewIndex(request):
    most_liked = Post.objects.filter(likes__gte = 1).order_by('-likes')[:3]
    posts_list = Post.objects.filter(date__lte = timezone.now()).order_by('-date')[:100]
    posts = []

    if request.method == 'GET':
        for post in posts_list:
            posts.append(post)

        for liked in most_liked:
            for post in posts:
                if liked.title == post.title:
                    posts.remove(post)

        likePost = request.GET.get('like', None)

        if likePost is not None:
            for post in posts:
                if post.title == likePost:
                    post.likes += 1
                    post.save()

    # Passing an object list so the if will need to use .count than |length
    return render(request, 'blog/view/index-content.html', {'posts': posts, 'liked_posts': most_liked})


def viewPost(request, title):
    post            = Post.objects.get(title = title)
    recent_posts    = Post.objects.filter(date__lte = timezone.now()).order_by('-date')[:10]

    comments        = Comment.objects.filter(post = post)
    reply_comment   = None

    if request.method == 'POST':
        print("Post Method")
        username    = request.POST['username']
        email       = request.POST['email']
        message     = request.POST['message']
        reply_id    = -1

        if request.POST['reply_comment'] != "":
            reply_id = request.POST['reply_comment']

        comment = Comment(post = post, username = username, email = email, message = message, reply_id = reply_id, date = timezone.now())
        comment.save()

        post.comments += 1
        post.save()

        return render(request, 'blog/view/post.html', {'post': post, 'posts': recent_posts, 'comments': comments, })
    else:
        print("Get Method")

        reply_id = request.GET.get('replyTo', None)

        if reply_id is not None:
            for comment in comments:
                if str(reply_id) == str(comment.id):
                    reply_comment = comment

        # Passing an array so the if will need to use |length than count
        return render(request, 'blog/view/post.html', {'post': post, 'posts': recent_posts, 'comments': comments, 'reply_comment': reply_comment, })


def viewSearchCategory(request, search):
    query_set = Post.objects.all()
    posts = []

    for query in query_set:
        for x in range(len(query.get_categories())):
            if search == query.get_categories()[x]:
                posts.append(query)

    # Passing an array so the if will need to use |length than count
    return render(request, 'blog/view/search.html', {'posts': posts, 'search': search, })


def viewSearchAuthor(request, search):
    posts = Post.objects.filter(author = search).order_by('-date')

    # Passing an array so the if will need to use |length than count
    return render(request, 'blog/view/search.html', {'posts': posts, 'search': search, })


def viewSearch(request):
    query_set = Post.objects.all().order_by('-date')
    posts = []
    search = None

    if request.method == 'POST':
        search = request.POST['search']

        for post in query_set:
            if search in post.title or search in post.content or search in post.headerTitle or search in post.author:
                posts.append(post)

    # Passing an array so the if will need to use |length than count
    return render(request, 'blog/view/search.html', {'posts': posts, 'search': search, })


def search_titles(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''

    posts = Post.objects.filter(title__contains = search_text)

    return render_to_response('blog/include/ajax_search.html', {'posts': posts})


def like_post(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        user_ip = request.POST['user_ip']
        update  = request.POST['update']
    else:
        post_id = -1
        user_ip = -1
        update  = -1

    post = Post.objects.get(id = post_id)
    liked_post = False

    if user_ip in post.get_liked():
        if update == 'true':
            # Since we can't manipulate the string itself we need to store it in a
            # temp variable and re assign it
            new_liked = post.liked.replace(user_ip + ',', '')
            post.liked = new_liked
            post.update_likes(-1)
            liked_post = False
        else:
            liked_post = True
    else:
        if update == 'true':
            post.liked += user_ip + ","
            post.update_likes(1)
            liked_post = True
        else:
            liked_post = False

    if update == 'true':
        post.save()

    return render_to_response('blog/include/post_likes.html', {'post': post, 'liked_post': liked_post, 'user_ip': user_ip, })
