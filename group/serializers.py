from rest_framework import serializers

from group.models import Group, Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    users = PersonSerializer(many=True, read_only=True)
    # admins = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'
        extra_kwargs = {
            # 'admins': {'required': False},
            'users': {'required': False},
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
