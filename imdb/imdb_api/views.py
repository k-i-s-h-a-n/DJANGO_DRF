from django.shortcuts import render,HttpResponse

# Create your views here.


def homePage(request):
    return HttpResponse("houisdfhouen fwjdsio fre fjwip erf fjwp ")

def movie_list(request):
    return HttpResponse("testing list")

def movie_detail(request,pk):
    return HttpResponse("testing movie detail")