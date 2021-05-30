from django.shortcuts import render
from .models import Person



#def GetPersonById(id):
#    Person.objects.get(id=id)

def get_all_persons(request):
    persons = Person.objects.all()
    return render(request, 'person/person_listing.html', {'persons': persons})
