__author__ = 'Tyler Walker' # twalker1998@gmail.com
from hashlib import md5

from allauth.account.adapter import get_adapter
from allauth.account.views import ConfirmEmailView, app_settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from api.serializer import UserSerializer

# Login required mixin
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class APIRoot(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        return Response({
            'OBIS': {
                'Tables': [ # TODO: why can't I reverse any of the views I wrote?
                    reverse('acctax-list', request=request),
                    reverse('comtax-list', request=request),
                    reverse('syntax-list', request=request),
                    reverse('occurrence-list', request=request),
                    reverse('source-list', request=request),
                    reverse('hightax-list', request=request),
                    reverse('fedstatus-list', request=request),
                    reverse('ststatus-list', request=request),
                    reverse('okswap-list', request=request),
                    reverse('institution-list', request=request),
                    reverse('county-list', request=request),
                    reverse('cotrs-list', request=request),
                    reverse('identificationverification-list', request=request),
                    reverse('rankchange-list', request=request),
                    reverse('spatialrefsys-list', request=request)
                ]
            },
            'User Profile': {
                'User': reverse('user-list', request=request)
            }
        })

class CustomConfirmEmailView(ConfirmEmailView):
    def get(self, *args, **kwargs):
        # Simply call the view's post function so the user's email will be confirmed.
        return self.post()
    
    def post(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)

        # In the event someone clicks on an email confirmation link
        # for one account while logged into another account,
        # logout of the currently logged in account.
        if (
            self.request.user.is_authenticated
            and self.request.user.pk != confirmation.email_address.user_id
        ):
            self.logout()

        get_adapter(self.request).add_message(
            self.request,
            messages.SUCCESS,
            "account/messages/email_confirmed.txt",
            {"email": confirmation.email_address.email},
        )
        if app_settings.LOGIN_ON_EMAIL_CONFIRMATION:
            resp = self.login_on_confirm(confirmation)
            if resp is not None:
                return resp
        # Don't -- allauth doesn't touch is_active so that sys admin can
        # use it to block users et al
        #
        # user = confirmation.email_address.user
        # user.is_active = True
        # user.save()
        redirect_url = self.get_redirect_url()
        if not redirect_url:
            ctx = self.get_context_data()
            return self.render_to_response(ctx)
        return redirect(redirect_url)
    
    def get_redirect_url(self):
        # Redirect the user to the login page on the front end.
        return 'https://obis.ou.edu/collaborators/login?returnUrl=/collaborators/search/main&verify=true'

class UserProfile(LoginRequiredMixin, APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class   = UserSerializer
    fields             = ('username', 'first_name', 'last_name', 'email')
    model              = User

    def get(self, request, id=None, format=None):
        data                  = User.objects.get(pk=self.request.user.id)
        serializer            = self.serializer_class(data, context={'request': request})
        tok                   = Token.objects.get_or_create(user=self.request.user)
        rdata                 = serializer.data
        rdata['name']         = data.get_full_name()
        rdata['gravator_url'] = '{0}://www.gravatar.com/avatar/{1}'.format(request.scheme,md5(rdata['email'].strip(' \t\n\r')).hexdigest())
        rdata['auth-token']   = str(tok[0])

        return Response(rdata)

    def post(self, request, format=None):
        user     = User.objects.get(pk=self.request.user.id)
        password = request.DATA.get('password', None)

        if password:
            user.set_password(password)
            user.save()
            data = {'password': 'Successfully Updated}'}

            return Response(data)

        auth_tok = request.DATA.get('auth-token', None)

        if str(auth_tok).lower() == 'update':
            tok = Token.objects.get(user=user)
            tok.delete()

            tok  = Token.objects.get_or_create(user=self.request.user)
            data = {'auth-token': str(tok[0])}

            return Response(data)
        else:
            user.first_name = request.DATA.get('first_name', user.first_name)
            user.last_name  = request.DATA.get('last_name', user.last_name)
            user.email      = request.DATA.get('email', user.email)
            serializer      = self.serializer_class(user, context={'request': request})
            data            = serializer.data
            user.save()

            tok                  = Token.objects.get_or_create(user = self.request.user)
            data['name']         = user.get_full_name()
            data['gravator_url'] = '{0}://www.gravatar.com/avatar/{1}'.format(request.scheme,md5(data['email'].strip(' \t\n\r')).hexdigest())
            data['auth-token']   = str(tok[0])

            return Response(data)

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request, so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the owner of the object.
        return obj.owner == request.user
