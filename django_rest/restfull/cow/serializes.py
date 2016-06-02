from rest_framework import serializers

from cow.models import User,Post


class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('firstname','username','password','email','joined')

class PostSerialize(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = {'title','content','date_created','email','joined'}
