from posts.models import Post
from posts.api.serializers import PostListSerializer, PostDetailSerializer


"""
Create
"""
data = {
    "title": "Yeah dude",
    "content": "New Content Here Dude",
    "slug": "yeah-dude",
    "publish": "2016-2-12"
}

new_item = PostListSerializer(data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)


"""
Update
"""
data = {
    "title": "New Item",
    "content": "New Content Here",
    "slug": "new-item",
    "publish": "2016-2-12"
}

obj = Post.objects.get(id=2)

new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)
