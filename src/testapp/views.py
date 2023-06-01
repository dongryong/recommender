from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
""" views for testapp"""

class Pong(View):
    def get(self,request):
        """ handle get request"""
        return HttpResponse("pong")
    
@require_http_methods(["GET","HEAD","OPTIONS"])
def pong(request):
    """ respon to Ping"""    
    if request.method in ["GET","HEAD"]:
        return HttpResponse("pong")
    else:
        response = HttpResponse()
        response["Allow"] = ", ".join([
            "GET","HEAD","OPTIONS"
        ])
        return response