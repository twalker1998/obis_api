from rest_framework import permissions, viewsets
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer

from .models import InviteUser
from .serializer import InviteUserSerializer

class CheckUUIDView(viewsets.ModelViewSet):
    model              = InviteUser
    serializer_class   = InviteUserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes   = (BrowsableAPIRenderer, JSONRenderer)

    def get_queryset(self):
        if self.request.method == 'GET':
            id = self.request.GET.get('id', '')
            return InviteUser.objects.filter(id__exact=id)
