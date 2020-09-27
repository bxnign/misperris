from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
#MENSAJES
from django.contrib import messages
#Importamos los modelos de los perros
from .models import Perros_Rescatados
#Importamos el Formulario 
from .forms import Perro_RescatadoForm

#Para redirigir las vistas 
from django.contrib.auth.decorators import login_required, permission_required



# Create your views here.
#Devolver a la pagina de inicio
def inicio(request):
	# Se van agregar los post a la platilla.html
    perros = Perros_Rescatados.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'perris/inicio.html',  {'perros': perros})
       



#Metodo que nos redirecciones a un sition para cada tipo de usuario

def redirigir(request):

    user = request.user
    perros = Perros_Rescatados.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    if user.has_perm('perris.admin'):
        return render(request, 'perris/inicio.html', {'perros': perros}) 
    else:
        return render(request, 'perris/inicio.html',{'perros': perros})   


def login(request):
    return render(request, 'registration/login.html', {})

def perros_disponibles(request):
	#Mostrar los perros disponibles 
	# Se van agregar los post a la platilla.html
    # Hacer que en la lista aparezcan solo los usuarios disponibles 
    perros = Perros_Rescatados.objects.filter( estado="Disponible")
    return render(request, 'perris/perros_disponibles.html', {'perros': perros})




def administrador(request):
    perros = Perros_Rescatados.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'perris/administrador.html', {'perros': perros})


#Vista del Agregar un nuevo post de perro rescatadoo
def agregarperro(request):
    form = Perro_RescatadoForm()
    return render(request, 'perris/agregarperro.html', {'form': form})



#Guardar los datos del Formulario del Perro rescatado en la BD 
def agregarperro(request):
   if request.method == "POST":
       form = Perro_RescatadoForm(request.POST or None , request.FILES or None)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.published_date = timezone.now()
           post.save()
           messages.info(request, 'El Perro se agregó correctamente!')
           return redirect('adm.inicio')
   else:
       form = Perro_RescatadoForm()
   return render(request, 'perris/agregarperro.html', {'form': form})

#Ver mas detalles del Post Perro
#Detalle del Post
def detallesperro(request, pk):
    perros = get_object_or_404(Perros_Rescatados, pk=pk)
    return render(request, 'perris/detallesperro.html', {'perro': perros})

#Modificar el POST de Perros y guardarlo
def editarperro(request, pk):
    post = get_object_or_404(Perros_Rescatados, pk=pk)
    if request.method == "POST":
        form = Perro_RescatadoForm(request.POST or None , request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # return redirect('detail_post_perro', pk=post.pk)
            messages.info(request, 'La informacion del  perro se actualizo')
            return redirect('adm.inicio')
    else:
        form = Perro_RescatadoForm(instance=post)
    return render(request, 'perris/editarperro.html', {'form': form})

#Eliminar el post del perro
def eliminarperro (request , pk):
    perros=Perros_Rescatados.objects.get(pk=pk)
    if request.method =="POST":
        perros.delete()
        messages.info(request, 'El Perro ah sido eliminado')
        return redirect ('adm.inicio')
    return render(request, 'perris/eliminarperro.html', {'perro': perros})