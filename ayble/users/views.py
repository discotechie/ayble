from rest_framework import viewsets
from users.models import CustomUser
from users.serializers import UserList, UserDetail
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()

    def get_queryset(self):
        user = self.request.user
        # only show the response if requesting user = user requested
        # or if the user is superuser
        if self.action == 'retrieve' and not user.is_superuser:
            return CustomUser.objects.filter(email=user)
        return CustomUser.objects.all()

    # list should have smaller response
    # retrieve has more detail about the user
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetail
        return UserList