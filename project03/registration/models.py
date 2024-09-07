from django.db import models

# Create your models here.


class Students(models.Model):
    stuid = models.IntegerField()
    name = models.CharField(max_length=30)
    program = models.CharField(max_length=20)
    city = models.CharField(max_length=40)

# To indentifyy the record in table we use this method
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['stuid']  # Orders students by name in ascending order
