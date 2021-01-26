from django.urls import path
from .views import PostsView, PostsDetailView, PostsUpdateView, DeletePostsView, DeleteCommentView

app_name = 'feed'

urlpatterns = [
    path('', PostsView.as_view(), name='allPosts'),
    path('post/<int:pk>', PostsDetailView.as_view(), name='detailPost'),
    path('post/update/<int:pk>', PostsUpdateView.as_view(), name='updatePost'),
    path('post/delete/<int:pk>', DeletePostsView.as_view(), name='deletePost'),
    path('post/<int:post_pk>/comments/delete/<int:pk>/' , DeleteCommentView.as_view(), name='deleteComment'),

]
