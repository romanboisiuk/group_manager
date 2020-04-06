from rest_framework import viewsets

from group.models import Group, Person
from group.serializers import GroupSerializer, PersonSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    # def get(self, request, pk):
    #     user = request.user.pk
    #     queryset = Group.objects.filter(super_admin=user, pk=pk)
    #     serializer = GroupSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     data = {
    #         'name': request.data['name'],
    #         'super_admin': request.user.pk,
    #     }
    #     serializer = GroupSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request):
    #     data = {
    #         'name': request.data['name'],
    #         'super_admin': request.user.pk,
    #     }
    #     serializer = GroupSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request):
    #     user = request.user.pk
    #     qroup = request.data['group']
    #     role = request.data['role']
    #     is_user_group_owner = Group.objects.filter(
    #         Q(super_admin=user) & Q(name=qroup)
    #     ).values()
    # if is_user_group_owner:
    #     if role == 'admin':

    # data = {
    #     'group': '',
    #     'users': [],
    #     'role': '',
    # }
