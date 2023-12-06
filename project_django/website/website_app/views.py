from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, "landing/index.html")
def acercadenosotros(request):
    return render(request, "landing/acercadenosotros.html")
def contactanos(request):
    return render(request, "landing/contactanos.html")
def faq(request):
    return render(request, "landing/FAQ.html")
def suscripcion(request):
    return render(request, "landing/suscripcion.html")
def base(request):
    return render(request, "landing/base.html")
def nacional(request):
    return render(request, "landing/nacional.html")
