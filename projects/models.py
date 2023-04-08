from django.db import models




# Create your models here.
class Projects(models.Model):
    input = models.CharField(max_length=500, blank=True, null=True)



    class Meta:
        verbose_name_plural = "Projects"


    def __str__(self):
        return self.name
