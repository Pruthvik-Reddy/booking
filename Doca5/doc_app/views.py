from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

def index(request):
    return render(request,"doc_app/slots.html")