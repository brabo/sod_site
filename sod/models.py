from django.db import models

# Create your models here.

class Stats(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    a = models.PositiveIntegerField()
    b = models.PositiveIntegerField()
    c = models.PositiveIntegerField()
    d = models.PositiveIntegerField()
    open = models.PositiveIntegerField()
    recursive = models.PositiveIntegerField()
    size = models.PositiveIntegerField()

    class Meta:
        db_table = 'ips'

    def show_ip(self):
	ip = str(self.a) + "." + str(self.b) + "." + str(self.c) + "." + str(self.d)
        return ip

#    def __unicode__(self):
#        return self.f
class Query(models.Model):
    country = models.CharField(max_length=50)

    class Meta:
        db_table = 'ips'

    def __unicode__(self):
        return self.country

