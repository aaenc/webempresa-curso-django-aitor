from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages  # Para mostrar mensajes al usuario
from .forms import ContactForm

# Create your views here.

def contact(request):
   contact_form = ContactForm()
   if request.method == "POST":
      contact_form = ContactForm(data=request.POST)
      if contact_form.is_valid():
         name=request.POST.get("name",'')
         email=request.POST.get("email",'')
         content=request.POST.get("content",'')
         # cargamos datos para enviar el EMail
         subject="La Caffetiera: Nuevo mensaje de contacto"
         body=f"De {name} <{email}>:\n\n{content}"
         from_email= settings.EMAIL_HOST_USER #"aaenc@yahoo.es"
         to= [settings.DEFAULT_FROM_EMAIL] #["aaenc@yahoo.es"] 
         bcc= None
         connection= None
         attachments = None
         headers = None #{'Reply-To': f"'{name} <{email}>'"} # email es el string del usuario
         cc = None
         reply_to = None #[f"{name} <{email}>"]
         # Enviamos el EMail
         correo=EmailMessage(subject,body,from_email,to,bcc,connection,attachments,headers,cc,reply_to)
         try:
            correo.send()
            # Muestra un mensaje amigable al usuario
            messages.success(request, "¡Tu mensaje ha sido enviado con éxito!")
            # Algo no ha ido OK
         except Exception as e:
            # Algo no ha ido bien
            # Para Debug
            messages.error(request, f"Error al enviar el mensaje: {str(e)}")
            # Muestra un mensaje amigable al usuario
            messages.error(request, "Hubo un problema al enviar tu mensaje. Inténtalo más tarde.")            # Algo no ha ido bien



   return render(request, "contact/contact.html",{'form': contact_form})
