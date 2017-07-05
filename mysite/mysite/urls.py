"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

### for picture !
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles


from django.conf.urls import url
from django.contrib import admin
### app add : step 4, import app 
from learn import views as learn_views
#!
#~ from django.conf.urls import include

urlpatterns = [
    #!
    #~ url(r'^grappelli/', include('grappelli.urls')),
    url(r'^$', learn_views.home, name='home'),
    url(r'^$', learn_views.dynamic_update, name='dynamic_update'),
    url(r'^admin/', admin.site.urls),
    
    
    #~ url(r'^$', learn_views.dynamic_update, name='dynamic_update'),
    ### add templates menu 
    #~ url(r'^$', learn_views.menu, name='menu'),
    
    
    ### add templates : step 4
    #~ url(r'^$', learn_views.home, name='home'),
    ### add templates : step 5, connect to db ---> python manage.py migrate
    
    
    ### app add : step 5
    # add to urls
    #~ url(r'^$', learn_views.index),
]


