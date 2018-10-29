from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import wikipedia as wiki

# Create your views here.
from django.views import View


def search_form(request):
    return render(request, 'basic_search/search_form.html')


def search(request):
    result=''
    try:
        result = wiki.page(title=request.GET['q']).html()
    except wiki.exceptions.DisambiguationError(title=request.GET['q'], may_refer_to=wiki.search(request.GET['q'])):
        pass
    # s = wiki.random(e.options)
    # HttpResponse("try searching:")
    # result = '\n'.join(wiki.search(request.GET['q']))
    except:
        return HttpResponse('You submitted an empty form')
    return HttpResponse(result)
