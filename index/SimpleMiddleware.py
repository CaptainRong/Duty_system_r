from django.shortcuts import redirect


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        open_urls = ['/admin/login/', '/admin/logout/']
        if not request.user.is_authenticated and request.path_info not in open_urls:
            return redirect('/admin/login/')
        response = self.get_response(request)
        return response
