from django.shortcuts import render

## It used to provide instant HTML code generation within Python files
from django.http import HttpResponse


# Create your views here.

def HttpResp(request):
    return HttpResponse("Test the HttpResponese")

def HTML_page(request):

    ## create the dynamic page input
    test = { 't1':34,'t2':35,'t3':24}

    # We created a content dictionary to send information to the HTML page
    return render(request, "test_template_APP/index.html" , context = { 'test' :test})



    