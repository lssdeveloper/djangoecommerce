from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    texts = ['Lorem ipsum sit amet', 'consectur adipiscing elit']
    context = {
        'title' : 'Django E-commerce',
        'teste' : 'Teste Context',
        'texts' : texts
    }
    return render(request, 'index.html', context)