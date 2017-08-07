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

from highcharts.views import HighChartsBarView


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

#~ def dynamic_update(request):
    #~ dy_data = mymodel.objects.filter(xxx='111')
    #~ dy_id = dy_data.aggregate(Max('id'))
    #~ dy_max_data = mymodel.objects.filter(id=dy_id['id__max'])
    #~ html = ''
    #~ json_serializer = serializers.get_serializer("json")()
    #~ html += json_serializer.serialize(dy_max_data)
    #~ return HttpResponse(html,mimetype="text/json")


def home(request):
    post_list = Post.objects.all()
    article_list = Article.objects.all()
    return render(request, 'home.html', locals())
