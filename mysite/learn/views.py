### always need !
# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django import template

### templates  ---> render_to_response
#~ from django.shortcuts import render_to_response

### for picture ! step 4.
from learn.models import Post
from learn.models import Article

# from highcharts.views import HighChartsBarView


#~ class BarView (HighChartsBarView):
    #~ categories = ['Orange', 'Bananas', 'Apples']

    #~ @property
    #~ def series(self):
        #~ result = []
        #~ for name in ('Joe', 'William', 'Averell'):
            #~ data = []
            #~ for x in xrange(len(self.categories)):
                #~ data.append(random.randint(0,10))
            #~ result.append({'name':name, "data":data})
        #~ return result

def dynamic_update(request):
    dy_data = mymodel.objects.filter(xxx='111')
    dy_id = dy_data.aggregate(Max('id'))
    dy_max_data = mymodel.objects.filter(id=dy_id['id__max'])
    html = ''
    json_serializer = serializers.get_serializer("json")()
    html += json_serializer.serialize(dy_max_data)
    return HttpResponse(html,mimetype="text/json")


def home(request):
    post_list = Post.objects.all()
    article_list = Article.objects.all()
    return render(request, 'home.html', locals())
    

#~ def home(request):
    #~ post_list = Post.objects.all()
    #~ return render(request, 'home.html', {'post_list': post_list,})
    
#~ def home(request):
    #~ article_list = Article.objects.all()
    #~ return render_to_response('db.html', locals())


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

#~ def index(request):
    #~ return HttpResponse(u"歡迎光臨 CO2 Conc.")
