#it requires request client
#response should be received from your server to your client

from django.http import HttpResponse
import datetime

def index_display(requests):
    date = datetime.datetime.now()
    print("This is our first page -  home page")
    return HttpResponse("<h1> This is index page, and this is h1 tag</h1>" + str(date)) 
# we are returning a response from server in para - h1

#Create multiple urls - pages
def about(request):
    return HttpResponse("<h1>This is about page</h1>")

#def contact_us(request):
 #   return HttpResponse("<h1>This is contact us page, and this is h1 tag</h1>" 
  #                      +'<h2>this is h2 tag</h2>'
   #                     + '<h3>this is h3 tag</h3>'
    #                    +'<h4>this is h4 tag</h4>'
     #                   +'<h5>this is h5 tag</h5>'
      #                  +'<h6>this is h6 tag</h6>')
    
from django.shortcuts import render   
def index(request):
    return render(request, 'index.html')

def contact_us(request):
    return render(request, 'contact_us.html', {})