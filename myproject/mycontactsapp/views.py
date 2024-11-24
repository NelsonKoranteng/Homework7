

# Create your views here.
from django.shortcuts import render
from .models import Contact

def index(request):
    contacts = Contact.objects.order_by('first_name')  # Sort alphabetically
    return render(request, 'index.html', {'contacts': contacts})
        # Henry Fox
        # James Brown
        # Kate Charnes
        # Make sure the list is alphabetically sorted.