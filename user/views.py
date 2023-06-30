from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView

# Create your views here.
class Me(APIView):

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)