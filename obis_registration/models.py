import uuid
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.db import models

class InviteUser(models.Model):
    id    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=False, null=False)

    def __str__(self):
        return self.email

    def save(self):
        if self.id and self.email:
            if User.objects.filter(email__exact=self.email):
                raise ValidationError({'email': ["This email has already been registered with OBIS.",]})
            message = 'Click here to register for OBIS: ' + 'https://obis.ou.edu/user-portal/register/?id=' + str(self.id)
            send_mail('Register for OBIS', message, 'obis.noreply@gmail.com', [self.email])
        super(InviteUser, self).save()
