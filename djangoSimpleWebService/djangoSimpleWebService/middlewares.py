# from django.utils.deprecation import MiddlewareMixin
#
#
# class CustomMiddle(MiddlewareMixin):
#
#     def __int__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         response = self.get_response(request)
#         response["X-Frame-Options"] = "X"
#         response["X-Content-Type-Options"] = "X"
#         response["Referrer-Policy"] = "X"
#         response["Cross-Origin-Opener-Policy"] = "X"
#         return response
#
#
