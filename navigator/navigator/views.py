# I have created this file-Chandan
from django.http import HttpResponse


def navigation(request):
    sites = ['''<h1>Entertainment </h1><a href="http://www.youtube.com"> Youtube Videos</a>''',
             '''<h1>Searching </h1><a href="http://www.google.com"> Google search engine</a>''',
             '''<h1>To Learn </h1><a href="http://www.w3school.com"> W3school</a>''',
             '''<h1>Social Media</h1><a href="http://www.facebook.com"> Facebook</a>''',
             '''<h1>Online Shopping </h1><a href="http://www.flipcart.com"> Shopping</a>''']
    return HttpResponse((sites))
