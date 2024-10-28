from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comentario
from .forms import ComentarioForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.conf import settings  # Importar settings


# Front page con los posts
def index(request):
    posts = Post.objects.all().order_by('-fecha_creacion')
    return render(request, 'index.html', {'posts': posts})

# Detalle de un post
def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.vistas += 1  # Incrementar el contador de visitas
    post.save()
    comentarios = post.comentarios.all()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.post = post
            comentario.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = ComentarioForm()

    return render(request, 'detalle_post.html', {'post': post, 'comentarios': comentarios, 'form': form})

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('file'):
        image = request.FILES['file']
        file_name = default_storage.save(f"uploads/{image.name}", image)
        image_url = f"{settings.MEDIA_URL}{file_name}"
        return JsonResponse({'location': image_url})
    return JsonResponse({'error': 'Error uploading image'}, status=400)