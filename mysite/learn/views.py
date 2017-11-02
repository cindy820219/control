### always need !
# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django import template

### for picture ! step 4.
from learn.models import Post
from learn.models import Article

import json
import time


from random import randint
from django.views.generic import TemplateView

sensors = {}


def dynamic_update(request):
    
    print(sensors.keys())
    
    for key in sensors.keys():
        print(sensors[key])
    
    Count = 0
    Sensor = 4
    #~ tm = time.strftime("%H:%M:%S")
    tm = time.time()
    CO2 = 440
    
    data = {'Count':Count, 'Sensor':Sensor,  'Time':tm, 'CO2':CO2}

    return JsonResponse(data)


def home(request):
    post_list = Post.objects.all()
    article_list = Article.objects.all()
    return render(request, 'home.html', locals())


# http://127.0.0.1:8000/pd?id=4&type=co2&value=440
def push_data(request):
    sensor_id = str(request.GET.get('id'))
    sensor_type = request.GET.get('type')	# co2 or hum or temp
    value = int(request.GET.get('value'))
    update_time = time.time()
    
    if not(hasattr(sensors, str(sensor_id))):
        sensors[sensor_id] = {}
    
    if not(hasattr(sensors[sensor_id], 'co2')):
        sensors[sensor_id]['co2'] = []
    
    tmp_data = {'time':update_time, 'value': value}
    
    tmp = sensors[sensor_id]['co2'].copy()
    tmp.append(tmp_data.copy())
    print('TMPPPPPPPP============')
    print(tmp)
    
    sensors[sensor_id]['co2'] = tmp.copy()
    print("PDDDDD")
    print(sensors[sensor_id]['co2'])
    
    data = {'id':sensor_id, 'time':update_time, 'type':sensor_type, 'value': value}
    #~ data = 

    return JsonResponse(data)
    
