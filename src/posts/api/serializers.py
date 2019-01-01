from rest_framework import serializers

from posts.models import Post

from comments.api.serializers import CommentSerializer
from comments.models import Comment

from accounts.api.serializers import UserDetailSerializer

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # 'id',
            'title',
            # 'slug',
            'content',
            'publish',
        ]


class PostDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    image = serializers.SerializerMethodField()
    html = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'content',
            'html',
            'image',
            'publish',
            'comments',
        ]

    def get_html(self, obj):
        return obj.get_markdown()

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_comments(self, obj):
        # content_type = obj.get_content_type
        # object_id = obj.id
        comments_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(comments_qs, many=True).data
        return comments


class PostListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='posts-api:detail',
        lookup_field='slug')
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            # 'slug',
            'content',
            'publish',
        ]
