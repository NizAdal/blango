from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
import logging.config
# from blog.forms import CommentForm

logger = logging.getLogger(__name__)


def index(request):
    # posts = Post.objects.filter(published_at__lte=timezone.now())
    posts = Post.objects.all()
    logger.debug("Got %d posts", len(posts))

    return render(request, "blog/index.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                return redirect(request.path_info)
                logger.info(
                  "Created comment on Post %d for user %s", post.pk, request.user
                )
        else:
            comment_form = CommentForm()
    else:
        comment_form = None

    return render(
        request, "blog/post-detail.html", {"post": post, "comment_form": comment_form}
    )

