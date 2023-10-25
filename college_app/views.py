from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'college_app/main.html')


def viewCollege(request, pk):
    return render(request, 'college_app/body.html')


def iitbombay(request):
    return render(request, 'college_app/iit_bombay.html')


def vitbhopal(request):
    return render(request, 'college_app/vit_bhopal.html')


def iitdelhi(request):
    return render(request, 'college_app/iit_delhi.html')


def iitdhanbad(request):
    return render(request, 'college_app/iit_dhanbad.html')


def iitgoa(request):
    return render(request, 'college_app/iit_goa.html')


def vitchennai(request):
    return render(request, 'college_app/vit_chennai.html')


def iitgandhinagar(request):
    return render(request, 'college_app/iit_gandhinagar.html')


def iitguwahati(request):
    return render(request, 'college_app/iit_guwahati.html')


def iitroorkee(request):
    return render(request, 'college_app/iit_roorkee.html')


def iitjodhpur(request):
    return render(request, 'college_app/iit_jodhpur.html')


def iitkanpur(request):
    return render(request, 'college_app/iit_kanpur.html')


def iitpatna(request):
    return render(request, 'college_app/iit_patna.html')


def nirfranking(request):
    return render(request, 'college_app/nirf ranking.html')


def vitvellore(request):
    return render(request, 'college_app/vit_vellore.html')


def vitamaravati(request):
    return render(request, 'college_app/vit_amaravati.html')


def about(request):
    return render(request, 'college_app/about.html')
