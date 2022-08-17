from explodindoMentes.models import *
class Course(models.Model):
    name = models.CharField(null=False, max_length=255)
    Description = models.TextField(null=False, max_length=255)
    Url = models.CharField(null=False, max_length=255)
    workload = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)

   
    def __str__(self):

       return '{}'.format(self.name)

   

   