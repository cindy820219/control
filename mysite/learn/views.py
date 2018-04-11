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

### new !
def test(data):
    # open CO2 file, and read the last line
    Fail = 0
    f = open('/home/nien/桌面/data/Dec07_CO2_5.txt','r')
    lines = f.readlines() 
    last_line = lines[-1]
    last_line_split = last_line.split(',')
    
    ### check data, if data fail --> Fail = 1!
    if len(last_line_split) != 4 or last_line_split[3] =='\n':
        print('Fail')
        Fail = 1

    if Fail == 0:
        data['Count'] = last_line_split[0]
        data['Sensor'] = last_line_split[1]
        data['CO2'] = last_line_split[3]

    return(data)
### new !

def dynamic_update(request):
    ### no idea
    print(sensors.keys())
    for key in sensors.keys():
        print(sensors[key])
    
    Count = 0
    Sensor = 0
    CO2 = 0
    tm = time.time()
    #~ tm = time.strftime("%H:%M:%S")
    
    print('---------------')
    data = {'Count':Count, 'Sensor':Sensor,  'Time':tm, 'CO2':CO2}
    
    ### new add!
    data = test(data)
    #~ print(data)

    return JsonResponse(data)

def home(request):
    post_list = Post.objects.all()
    article_list = Article.objects.all()
    return render(request, 'home.html', locals())


# http://127.0.0.1:8000/pd?id=4&type=co2&value=440
def push_data(request):
    
    ### no idea !
    sensor_id = str(request.GET.get('id'))
    sensor_type = request.GET.get('type')   # co2 or hum or temp
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
    
    
    ### new add!
    data = test(data)
    
    return JsonResponse(data)
    
