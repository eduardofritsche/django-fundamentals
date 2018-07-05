from django.shortcuts import render

def home(request):

  context = {
    'page_name':'Home Page',
    'element_list':[1,2,3,4,5],
    'element_name':'element name'
  }


  return render(request, 'home/home.html', context)
