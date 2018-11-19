from django.shortcuts import render, redirect
from collection.forms import JerseyForm
from collection.models import Jersey
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404

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

@login_required
def edit_jersey(request, slug):
    jersey = Jersey.objects.get(slug=slug)
    if jersey.user != request.user:
        raise Http404
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

def create_jersey(request):
    form_class = JerseyForm
    # if we're coming from a submitted form, do this 
    if request.method == 'POST':
        # grab the data from the submitted form and apply to 
        # the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but do not save yet
            jersey = form.save(commit=False)
            # set the additional details
            jersey.user = request.user
            jersey.slug = slugify(thing.name)
            # save the object
            jersey.save()
            # redirect to our newly created thing
            return redirect('thing_detail', slug=jersey.slug)
# otherwise just create the form
    else:
        form = form_class()
    return render(request, 'jerseys/create_jersey.html', { 
        'form': form,
})

def browse_by_name(request, initial=None):
    if initial:
        jerseys = Jersey.objects.filter(
            name__istartswith=initial).order_by('name')
    else:
        jerseys = Jersey.objects.all().order_by('name')
    return render(request, 'search/search.html', {
        'jerseys': jerseys,
        'initial': initial,
    })