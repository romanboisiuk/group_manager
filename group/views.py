from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from group.models import Group, User, Membership
from group.serializers import GroupSerializer, UserSerializer, MembershipSerializer
from rest_framework.response import Response
from rest_framework import status


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def update(self, request, *args, **kwargs):
        user = request.user.pk
        group_id = int(kwargs.get('pk'))
        group_owner = Group.objects.get(pk=group_id).super_admin.pk
        # membership = Membership.objects.filter(Q(member=user) & Q(group=group_id))

        if user == group_owner:
            data = self._update_admins_members(request.data, group_id)

            # TODO Check if is possible to refactor instance
            serializer = self.get_serializer(
                instance=self.get_object(),
                data=data,
                partial=kwargs.pop('partial', False)
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        return Response(
            {"detail": f"Request data {request.data}. is incorrect"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # TODO needs refactoring
    @staticmethod
    def _update_admins_members(data, group_id):
        data_to_update = {}
        group_admins = list(User.objects.filter(group_admins__pk=group_id).values_list('pk', flat=True))
        group_members = list(User.objects.filter(group_members__pk=group_id).values_list('pk', flat=True))
        new_admin_found = False
        new_member_found = False
        for member in data.get('admins', []):
            if member not in group_admins + group_members:
                new_admin_found = True
                group_admins.append(member)
        for member in data.get('members', []):
            if member not in group_admins + group_members:
                new_member_found = True
                group_members.append(member)
        if new_admin_found:
            data_to_update['admins'] = group_admins
        if new_member_found:
            data_to_update['members'] = group_members
        if data_to_update:
            return data_to_update

        return Response(
            {"detail": f"All members you are trying to add are already in group"},
            status=status.HTTP_406_NOT_ACCEPTABLE
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
