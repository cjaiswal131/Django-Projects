# I have created this file-Chandan
from django.http import HttpResponse
from django.shortcuts import render

def navigation(request):
    sites = ['''<h1>Entertainment </h1><a href="http://www.youtube.com"> Youtube Videos</a>''',
             '''<h1>Searching </h1><a href="http://www.google.com"> Google serch engine</a>''',
             '''<h1>To learn </h1><a href="http://www.w3school.com"> W3school</a>''',
             '''<h1>Social Media</h1><a href="http://www.facebook.com"> Facebook</a>''',
             '''<h1>Online shoping </h1><a href="http://www.flipcart.com"> SHoping</a>''']
    return HttpResponse((sites))

# def index(request):
#     return render(request, "index.html")
#     # return HttpResponse("Home")
#     # return HttpResponse('''<h1>Hi darling..!</h1> <a href="https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww">
#     # Djang CodeWithHarry</a>''')
