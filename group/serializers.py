from rest_framework import serializers

from group.models import Group, User


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name', 'super_admin', 'admins', 'members')
        extra_kwargs = {
            'admins': {'required': False},
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

    # def create(self, validated_data):
    #     return Group.objects.create(**validated_data)

# Serializers define the API representation.
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#
#
# class AuthorSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         ordering = ['-id']
#         model = Author
#         fields = ("id", "name", "biography", "date_of_birth", "books")
#         extra_kwargs = {'books': {'required': False}}
#
#
# class BookSerializer(serializers.ModelSerializer):
#     authors = AuthorSerializer(many=True, read_only=True)
#
#     class Meta:
#         ordering = ['-id']
#         model = Book
#         fields = ("id", "title", "description", "publisher", "release_date", "authors")
#         extra_kwargs = {'authors': {'required': False}}
