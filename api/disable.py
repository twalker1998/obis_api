class DisableCSRF(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)

