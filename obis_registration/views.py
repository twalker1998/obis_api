from obis.views import obisTableViewSet

from .models import InviteUser
from .serializer import InviteUserSerializer

class CheckUUIDView(obisTableViewSet):
    model            = InviteUser
    serializer_class = InviteUserSerializer

    def get_queryset(self):
        queryset = InviteUser.objects.all()

        if self.request.method == 'GET':
            id = self.request.GET.get('id', '')

            if id:
                queryset = queryset.filter(id__exact=id)

        return queryset
