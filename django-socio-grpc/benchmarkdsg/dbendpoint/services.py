from django_socio_grpc import generics

from dbendpoint.models import Post
from dbendpoint.serializers import PostProtoSerializer


# This service will have all the CRUD actions
class PostService(generics.AsyncModelService):
    queryset = Post.objects.all()
    serializer_class = PostProtoSerializer
