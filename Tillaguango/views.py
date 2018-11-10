from django.shortcuts import render_to_response, render 

def homePage(request):
	return render_to_response('home_Page.html')