from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from api.serializers import GroupSerializer, UserSerializer,CategorySerializer,BookSerializer,BorrowRecordSerializer
from library_app.models import Category,Book,Student,BorrowRecord


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ["list","retrive"]:
            return[permissions.AllowAny()]
        return super().get_permissions()
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("title")
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset

    def get_permissions(self):
        if self.action in ["list","retrive"]:
            return[permissions.IsAuthenticated()]
        return super().get_permissions()
    

# class BorrowRecordViewSet(viewsets.ModelViewSet):
#     queryset = BorrowRecord.objects.all()
#     serializer_class = BorrowRecordSerializer

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all().order_by("book")
    serializer_class = BorrowRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ["list","retrive"]:
            return[permissions.AllowAny()]
        return super().get_permissions()
  