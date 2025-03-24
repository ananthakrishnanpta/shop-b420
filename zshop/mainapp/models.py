from django.db import models

# Create your models here.
# Every Class defined here 
# inheriting the class models.Model from module django.db
# will become a table in the connected db.
# Automatic ORM capability is implemented in the inbuilt `Model` class
# After every change to this file, especially on creating new classes,
# or making changes to existing ones like changing attribute data,
# we have to run 

# python manage.py makemigrations <app_name>
# >> This will generate the python scripts necessary to make schema changes
# >> in the db.

# python manage.py migrate
# >> This will execute the scripts generated by the previous step

class Product(models.Model):
    # not going to override the __init__ method here
    # the inherited constructor has been coded to support ORM

    # We just list out the attributes of Product Entity type below
    # Additionally, for every model, django automatically generates
    # an `id` attribute which will act as primary key in the db
    # We can choose to use it instead of creating one ourselves.
    
    name = models.CharField(max_length=255) # VARCHAR
    price = models.FloatField()
    desc = models.TextField(max_length=500)
    img = models.ImageField(upload_to='products/')
    stock = models.PositiveIntegerField()

