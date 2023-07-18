from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import FormularioContacto
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,"correo/home.html")

def hello(request, username):
    return HttpResponse("<h1>Hello World %s</h1>" %username)

def about(request):
    return HttpResponse("About")

def correo(request):

    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje de app Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido), 
            '',
            ["efloressuc50@gmail.com"], 
            reply_to=[email])

            try:
                email.send()

                return redirect("/correo/?valido")
            except:
                return redirect("/correo/?novalido")

    return render(request, "correo/correo.html", {'miFormulario':formulario_contacto})
