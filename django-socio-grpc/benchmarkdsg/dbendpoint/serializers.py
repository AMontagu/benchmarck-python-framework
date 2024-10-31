from django_socio_grpc import proto_serializers
from dbendpoint.models import Post

class PostProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Post
        fields = "__all__"