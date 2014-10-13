from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext


# Create your views here.
def hello(request):
    return render_to_response('helloworld.html',  
                                context_instance=RequestContext(request)
    )