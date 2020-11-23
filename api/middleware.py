"""
Custom middleware used in the API.
"""

class DisableCSRFMiddleware:
    """
    Disables the CSRF requirement on API views.
    """
    def __init__(self, get_response) -> None:
        self.get_response = get_response
    
    def __call__(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True) # TODO: Should this be on the response?
        return self.get_response(request)

class DisableCORSMiddleware:
    """
    Disables the CORS requirement on API views.
    """
    def __init__(self, get_response) -> None:
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        response["Access-Control-Allow-Headers"] = "*"
        response["Access-Control-Allow-Methods"] = "*"
        response["Access-Control-Allow-Origin"] = "*"
        return response
