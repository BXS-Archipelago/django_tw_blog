from django.shortcuts import render


# function based views being used here -
def frontpage(request):
    return render(request, 'core/base.html')
