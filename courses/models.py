from django.db import models


class Course(models.Model):
    """ To add activity to the database """
    name = models.CharField(max_length=260, default='')
    short_description = models.TextField(default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    online_offer_price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

