from api import config

def title(request):
    return {'page_title': config.pageTitle, 'application_title': config.applicationTitle}
