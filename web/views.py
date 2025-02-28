from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render

# Create your views here.
def redirect_good(request):
    return HttpResponsePermanentRedirect("/redirect_result/")


def redirect_bad(request):
    response = HttpResponsePermanentRedirect("/redirect_result/")
    response.streaming = True
    return response


def redirect_result(request):
    return HttpResponse("It worked!")
