### always need !
# coding:utf-8

from django.shortcuts import render

### app add : step 2
from django.http import HttpResponse
from django import template

### templates  ---> render_to_response
from django.shortcuts import render_to_response

### for picture ! step 4.
from .models import Post


def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })




# --- Create your views here. --- #
### real template part 2 
#~ def menu(request):
    #~ food1 = {'name':'蕃茄','price':'60','is_spicy':False}
    #~ food2 = {'name':'蒜泥','price':'100','is_spicy':True}
    
    #~ foods = [food1, food2]
    
    #~ dic = {'1':'a', '2':'b'}
    
    #~ return render_to_response('menu.html',locals())


### real template !!!
#~ def home(request):
    #~ info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    #~ return render(request, 'tem.html', {'info_dict': info_dict})


### add templates : step 1, create file /app/templates/home.html
### add templates : step 2, add some html code in home.html
### add templates : step 3
#~ def home(request):
    #~ return render(request, 'home.html')

### app add : step 3
# print welcome
def index(request):
    return HttpResponse(u"歡迎光臨")

