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

from random import randint


sensors = {}
data = {
    1: {
        'co2': {
            'value': 0,
            'count': 0
        },
        'temp': {
            'value': 0,
            'count': 0
        },
        'hum': {
            'value': 0,
            'count': 0
        }
    },
    2: {
        'co2': {
            'value': 0,
            'count': 0
        },
        'temp': {
            'value': 0,
            'count': 0
        },
        'hum': {
            'value': 0,
            'count': 0
        }
    },
    3: {
        'co2': {
            'value': 0,
            'count': 0
        },
        'temp': {
            'value': 0,
            'count': 0
        },
        'hum': {
            'value': 0,
            'count': 0
        }
    },
    4: {
        'co2': {
            'value': 0,
            'count': 0
        },
        'temp': {
            'value': 0,
            'count': 0
        },
        'hum': {
            'value': 0,
            'count': 0
        }
    },
    5: {
        'co2': {
            'value': 0,
            'count': 0
        },
        'temp': {
            'value': 0,
            'count': 0
        },
        'hum': {
            'value': 0,
            'count': 0
        }
    },
    6: {
        'co2': {
            'value': 0,
            'count': 0
        },
        'temp': {
            'value': 0,
            'count': 0
        },
        'hum': {
            'value': 0,
            'count': 0
        }
    },
    7: {
        'co2': {
            'value': 0,
            'count': 0
        },
        'temp': {
            'value': 0,
            'count': 0
        },
        'hum': {
            'value': 0,
            'count': 0
        }
    },
    8: {
        'co2': {
            'value': 0,
            'count': 0
        },
        'temp': {
            'value': 0,
            'count': 0
        },
        'hum': {
            'value': 0,
            'count': 0
        }
    },
    9: {
        'co2': {
            'value': 0,
            'count': 0
        },
        'temp': {
            'value': 0,
            'count': 0
        },
        'hum': {
            'value': 0,
            'count': 0
        }
    },
}


def gen_data(req):
    # open CO2 file, and read the last line
    #~ Fail = 0
    #~ f = open('/home/nien/桌面/data/Dec07_CO2_5.txt','r')
    #~ lines = f.readlines() 
    #~ last_line = lines[-1]
    #~ last_line_split = last_line.split(',')
    
    ### check data, if data fail --> Fail = 1!
    #~ if len(last_line_split) != 4 or last_line_split[3] =='\n':
        #~ print('Fail')
        #~ Fail = 1

    #~ if Fail == 0:
        #~ data['']['CO2']['Count'] = last_line_split[0]
        #~ data['CO2']['Sensor'] = last_line_split[1]
        #~ data['CO2']['value'] = last_line_split[3].replace("\n", "")
        
    # print(randint(0, 9))
    
    #~ tmp = {
        #~ 'co2':{'value': 0, 'count':0},
        #~ 'temp':{'value': 0, 'count':0},
        #~ 'hum':{'value': 0, 'count':0}
    #~ }
    
    
    for sensor_id in range(1,10):
        
        tmp = {
            'co2':{'value': 0, 'count':0},
            'temp':{'value': 0, 'count':0},
            'hum':{'value': 0, 'count':0}
        }
        
        ### snesor 1 & sensor 2
        if sensor_id == 1 or sensor_id == 2:
            co2_random = randint(450, 460)
            hum_random = randint(85, 87)
            
            tmp['co2']['value'] = co2_random
            tmp['co2']['count'] = tmp['co2']['count'] + 1
            tmp['temp']['value'] = 15
            tmp['temp']['count'] = tmp['co2']['count']
            tmp['hum']['value'] = hum_random
            tmp['hum']['count'] = tmp['co2']['count']
        
            data[sensor_id] = tmp
            
        ### snesor 3 & sensor 4 & sensor 9    
        if sensor_id == 3 or sensor_id == 4 or sensor_id == 9:
            co2_random = randint(500, 510)
            hum_random = randint(87, 89)
            
            tmp['co2']['value'] = co2_random
            tmp['co2']['count'] = tmp['co2']['count'] + 1
            tmp['temp']['value'] = 15
            tmp['temp']['count'] = tmp['co2']['count']
            tmp['hum']['value'] = hum_random
            tmp['hum']['count'] = tmp['co2']['count']
        
            data[sensor_id] = tmp
        
        ### snesor 5
        if sensor_id == 5:
            co2_random = randint(470, 480)
            hum_random = randint(85, 87)
            
            tmp['co2']['value'] = co2_random
            tmp['co2']['count'] = tmp['co2']['count'] + 1
            tmp['temp']['value'] = 14
            tmp['temp']['count'] = tmp['co2']['count']
            tmp['hum']['value'] = hum_random
            tmp['hum']['count'] = tmp['co2']['count']
        
            data[sensor_id] = tmp            
            
        ### snesor 6
        if sensor_id == 6:
            co2_random = randint(490, 500)
            hum_random = randint(85, 87)
            
            tmp['co2']['value'] = co2_random
            tmp['co2']['count'] = tmp['co2']['count'] + 1
            tmp['temp']['value'] = 15
            tmp['temp']['count'] = tmp['co2']['count']
            tmp['hum']['value'] = hum_random
            tmp['hum']['count'] = tmp['co2']['count']
        
            data[sensor_id] = tmp         
            
        ### snesor 7
        if sensor_id == 7:
            co2_random = randint(520, 530)
            hum_random = randint(87, 89)
            
            tmp['co2']['value'] = co2_random
            tmp['co2']['count'] = tmp['co2']['count'] + 1
            tmp['temp']['value'] = 15
            tmp['temp']['count'] = tmp['co2']['count']
            tmp['hum']['value'] = hum_random
            tmp['hum']['count'] = tmp['co2']['count']
        
            data[sensor_id] = tmp         
        
        ### snesor 8
        if sensor_id == 8:
            co2_random = randint(530, 540)
            hum_random = randint(87, 89)
            
            tmp['co2']['value'] = co2_random
            tmp['co2']['count'] = tmp['co2']['count'] + 1
            tmp['temp']['value'] = 15
            tmp['temp']['count'] = tmp['co2']['count']
            tmp['hum']['value'] = hum_random
            tmp['hum']['count'] = tmp['co2']['count']
        
            data[sensor_id] = tmp
            
        del tmp

    #~ return(data)
    return JsonResponse(data)

def get_data ():
    return data

def dynamic_update(request):
    #~ print(sensors.keys())
    #~ for key in sensors.keys():
        #~ print(sensors[key])
    
    #~ Count = 0
    #~ Sensor = 0
    #~ CO2 = 0
    #~ tm = time.time()
    #~ tm = time.strftime("%H:%M:%S")
    
    #~ print('---------------')
    #~ data = {'Count':Count, 'Sensor':Sensor,  'Time':tm, 'CO2':CO2}
    
    ### delete ?
    #~ data = test(data)
    
    res = get_data()
    return JsonResponse(res)

def home(request):
    post_list = Post.objects.all()
    article_list = Article.objects.all()
    return render(request, 'home.html', locals())


# http://127.0.0.1:8000/pd?id=4&type=co2&value=440
def push_data(request):
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
    
    #~ data = 
    
    return JsonResponse(data)
