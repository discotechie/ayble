from rest_framework import viewsets
from users.models import CustomUser
from users.serializers import UserList, UserDetail
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()
    # overriding this method so that list view is more performant 
    # and retrieve has more detail about the user
    def get_serializer_class(self):
        if self.action == 'list':
            return UserList
        return UserDetail