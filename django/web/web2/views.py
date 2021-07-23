"""viws de python"""
import pdb
from django.http import HttpResponse
from datetime import datetime

from django.http.response import JsonResponse
def hola(request):
    now=datetime.now()
    
    return HttpResponse('hello fukin wordl bitch = {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))
def sorted(request):
    
    '''Retunr a sorted numbers in jason format'''
    
    numbers = map(lambda x : int(x),request.GET["numbers"].split(","))
    
    return JsonResponse({ "numbers" : sorted(numbers)},json_dumps_params={'indent': 4})
def say_hi(request,name,age):
    '''return  you are so young to joing or otherhand you are allowed to join'''
    if age <= 12:
        means="apoligaze {} you are so young".format(name)
    else:
        means="great {}you are allowed to join ".format(name)
    return HttpResponse(means)    
    
