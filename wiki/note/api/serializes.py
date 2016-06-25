from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField)
from note.models import (Post,
                         User)


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'posted',
        ]


class PostListSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'posted',
        ]




class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'posted',
        ]


class UserListSerializer(ModelSerializer):
    post = SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email',
            'post',
        ]

    def get_post(self, obj):
        return PostListSerializer(Post.objects.filter(user=obj),many=True).data