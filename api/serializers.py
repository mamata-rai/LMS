from django.contrib.auth.models import Group, User
from rest_framework import serializers
from library_app.models import Category,Book,Student,Teacher,BorrowRecord


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "groups","first_name","is_superuser"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # read_only_fields=["author"]

        # def validate(self,data):
        #     data["author"] = self.context["request"].user
        #     return data

class TeachertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "name"]

class StusentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class BorrowRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BorrowRecord
        fields ='__all__'