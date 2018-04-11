from django.db import models

# Create your models here.
### for picture ! 
class Post(models.Model):
    photo = models.URLField(blank=True)
    
    #~ def __str__(self):
        #~ return self.title

### 
class Article(models.Model):
    ##~ Sensor = models.TextField(u'Sensor')
    #~ Sensor = models.DecimalField(u'Sensor', max_digits = 2, decimal_places = 0)
    #~ Data = models.DecimalField(u'Data', max_digits = 10, decimal_places = 0)
    #~ Time = models.CharField(u'Time', max_length = 50)
    #~ Tpye = models.CharField(u'Tpye', max_length = 50)
    
    def __unicode__(self):
        return Time.Sensor
