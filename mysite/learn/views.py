### always need !
# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django import template

### for picture ! step 4.
from learn.models import Post
from learn.models import Article



from random import randint
from django.views.generic import TemplateView
# from chartjs.views.lines import BaseLineChartView




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
    

#~ class LineChartJSONView(BaseLineChartView):
    #~ def get_labels(self):
        #~ """Return 7 labels for the x-axis."""
        #~ return ["January", "February", "March", "April", "May", "June", "July"]

    #~ def get_providers(self):
        #~ """Return names of datasets."""
        #~ return ["Central", "Eastside", "Westside"]

    #~ def get_data(self):
        #~ """Return 3 datasets to plot."""

        #~ return [[75, 44, 92, 11, 44, 95, 35],
                #~ [41, 92, 18, 3, 73, 87, 92],
                #~ [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
#~ line_chart_json = LineChartJSONView.as_view()
