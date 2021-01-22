from django.shortcuts import render

# Create your views here.
def index(request):
	mypost=['Act1', 'Act2', 'Act3']
	return render(request,'Activity/index', {'posts': mypost})
