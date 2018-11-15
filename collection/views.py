from django.shortcuts import render
from collection.models import Thing #Tells the view we need information from the model

# Create your views here.
def index(request):
    things = Thing.objects.all() 
    return render(request, 'index.html', { #When index page is viewed, find all things in the database, display the template and pass those things along to that template
        'things': things,
    })

def thing_detail(request, slug):
    #grab the object
    thing = Thing.objects.get(slug=slug)
    #pass it to the template
    return render(request, 'things/thing_detail.html', {
        'thing': thing,
    })