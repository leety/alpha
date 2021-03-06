from django.conf.urls import url

from .views import (
    forums,
    forum_category,
    forum,
    forum_thread,
    post_create,
    reply_create,
    post_edit,
    subscribe,
    unsubscribe,
    thread_updates,
)


# Expected that these are mounted under namespace "pinax_forums"
urlpatterns = [
    url(r"^$", forums, name="forums"),
    url(r"^category/(\d+)/$", forum_category, name="category"),
    url(r"^forum/(\d+)/$", forum, name="forum"),
    url(r"^thread/(\d+)/$", forum_thread, name="thread"),
    url(r"^new_post/(\d+)/$", post_create, name="post_create"),
    url(r"^reply/(\d+)/$", reply_create, name="reply_create"),
    url(r"^post_edit/(thread|reply)/(\d+)/$", post_edit, name="post_edit"),
    url(r"^subscribe/(\d+)/$", subscribe, name="subscribe"),
    url(r"^unsubscribe/(\d+)/$", unsubscribe, name="unsubscribe"),
    url(r"^thread_updates/$", thread_updates, name="thread_updates"),
]
