from django.shortcuts import render, redirect
from collection.forms import JerseyForm
from collection.models import Jersey

def index(request):
    jerseys = Jersey.objects.all()
    return render(request, 'index.html', {
        'jerseys': jerseys, 
    })

def jersey_detail(request, slug):
    # grab the object...
    jersey = Jersey.objects.get(slug=slug)
    # and pass to the template
    return render(request, 'jerseys/jersey_detail.html', { 
        'jersey': jersey,
    })

def edit_jersey(request, slug):
    jersey = Jersey.objects.get(slug=slug)
    form_class = JerseyForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=jersey)
        if form.is_valid():
            form.save()
            return redirect('jersey_detail', slug=jersey.slug)
    else:
        form = form_class(instance=jersey)
    return render(request, 'jerseys/edit_jersey.html', {
        'jersey': jersey,
        'form': form,
    })