from rest_framework import serializers

from group.models import Group, User, Membership


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name', 'super_admin', 'members')
        extra_kwargs = {
            'members': {'required': False},
        }


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'groups')
        extra_kwargs = {
            'groups': {'required': False},
        }


class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = ('id', 'member', 'group', 'member_permission')
