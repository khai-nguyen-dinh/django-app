from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     RetrieveUpdateAPIView)
from note.models import Post, User
from .serializes import (PostCreateUpdateSerializer,
                         PostDetailSerializer,
                         PostListSerializer,
                         UserListSerializer)
from .pagination import PostLimitOffsetPagination,PostPageNumberPagination

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer

    def perform_user(self,serializer):
        serializer.save(user=self.request.user)


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostPageNumberPagination


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostDeletelAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostUpdatelAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailAPIView

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer