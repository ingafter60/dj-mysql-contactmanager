# import django modules
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView, DetailView

# import app files
from .models import Contact

class HomePageView(ListView):
	template_name 		= 'index.html'
	model 		  		= Contact 
	context_object_name = 'contacts' 

class ContactDetailView(DetailView):
	template_name 		= 'detail.html'
	model 				= Contact 
	context_object_name = 'contact'

# def search(request):
# 	context = {
	
# 	}
# 	return render(request, 'search.html', context)	

def search(request):
	if request.GET:
		search_term = request.GET['search_term']
		search_results = Contact.objects.filter(name__icontains=search_term)
		context = {
			'search_term': search_term,
			'contacts': search_results
		}
		return render(request, 'search.html', context)
	else:
		return redirect('home')	
