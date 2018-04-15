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

urlpatterns = [
    url(r'^$', learn_views.home, name='home'),
    url(r'^du$', learn_views.dynamic_update, name='dynamic_update'),
    url(r'^pd', learn_views.push_data, name='push_data'),
    url(r'^admin/', admin.site.urls),
    url(r'^gen_data', learn_views.gen_data, name='gen_data'),
]


