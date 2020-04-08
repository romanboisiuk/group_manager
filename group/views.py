from rest_framework import viewsets

from group.models import Group, User
from group.serializers import GroupSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def update(self, request, *args, **kwargs):
        user = request.user.pk
        group_id = int(kwargs.get('pk'))
        group_owner = Group.objects.get(pk=group_id).super_admin.pk
        if user == group_owner:


            # TODO Кверя завжди повертає super_admin_id
            group_users = list(User.objects.filter(group__pk=group_id).values_list('pk', flat=True))
            for _user in request.data['users']:
                if _user not in group_users:
                    group_users.append(_user)

            # TODO Check if is possible to refactor instance
            serializer = self.get_serializer(
                instance=self.get_object(),
                data={'users': group_users},
                partial=kwargs.pop('partial', False)
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        return Response(
            {"detail": f"Request data {request.data}. is incorrect"},
            status=status.HTTP_400_BAD_REQUEST
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
