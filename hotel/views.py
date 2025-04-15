from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.



def auctions(request):
    return render(request, 'auctions.html')


