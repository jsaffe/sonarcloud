from rest_framework.response import Response
from rest_framework.views import APIView
import os

class ContainerIdView(APIView):
    def get(self, request):
        container_id = os.getenv('HOSTNAME', 'Unknown')
        return Response({'container_id': container_id})