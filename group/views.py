from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from group.serializers import GroupSerializer


class CreateGroupView(APIView):
    def post(self, request):
        data = {
            'name': request.data['name'],
            'super_admin': request.user.pk,
        }
        serializer = GroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
