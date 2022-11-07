from django.shortcuts import render


# function based views being used here -
def frontpage(request):
    return render(request, 'core/frontpage.html')

def about(request):
    return render(request, 'core/about.html')