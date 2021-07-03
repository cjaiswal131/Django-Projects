from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}

    if extraspaceremover == "on":
        analyzed = ""
        djtext = djtext.strip()
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if charcount == 'on':
        analyzed = 0
        for char in djtext:
            analyzed += 1
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}

    if removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'on':
        return HttpResponse("Error:please select any operation and try again..")

    return render(request, 'analyze.html', params)
