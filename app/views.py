# import django modules
from django.shortcuts import render

# import app files
from .models import Contact

# Create your views here.
def home(request):
	context = {
		'contacts': Contact.objects.all()	
	}	
	return render(request, 'index.html', context)