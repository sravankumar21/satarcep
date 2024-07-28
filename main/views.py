from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def contestinfo(request):
    return render(request, 'main/contestinfo.html')

def contest(request):
    return render(request, 'main/contest.html')

def level2(request):
    return render(request, 'main/level2.html')

def level3(request):
    return render(request, 'main/level3.html')

def level4(request):
    return render(request, 'main/level4.html')

def level5(request):
    return render(request, 'main/level5.html')

def level6(request):
    return render(request, 'main/level6.html')

def level7(request):
    return render(request, 'main/level7.html')
