from rest_framework import serializers

from group.models import Group


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('name', 'super_admin')

    def create(self, validated_data):
        return Group.objects.create(**validated_data)
