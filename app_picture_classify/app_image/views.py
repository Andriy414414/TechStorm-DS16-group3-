from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 
                  template_name='app_image/index.html', 
                  context={'msg': 'project-team-5'})