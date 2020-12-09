from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

class CustomDefaultAccountAdapter(DefaultAccountAdapter):
    """
    Extend the `DefaultAccountAdapter` class from `allauth.account.adapter`
    to allow the API to send registration emails.
    """
    def send_mmail(self, template_prefix, email, context):
        context['activate_url'] = settings.URL_FRONT + 'verify/' + context['key']
        msg                     = self.render_mail(template_prefix, email, context)
        msg.send()
