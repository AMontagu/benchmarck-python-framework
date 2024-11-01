from django_socio_grpc import proto_serializers
from dbendpoint.models import Post
from dbendpoint.grpc.dbendpoint_pb2 import PostResponse, PostListResponse

class PostProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        proto_class = PostResponse
        proto_class_list = PostListResponse