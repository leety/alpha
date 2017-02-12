from django.db import models
# this will import the backend stuff so that fields are mapped database.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

# first_name and last_name are fields of the model.
    # Each field is specified as a class attribute, and each attribute maps to a database column.

# field options: https://docs.djangoproject.com/en/1.10/topics/db/models/


class Person2(models.Model):
    # By default, Django gives each model the following field, so self.id will always be automatically generate.
    id = models.AutoField(primary_key=True)

    # value given is the default;
    first_name = models.CharField(
        null=False,
        blank=False,
        choices=list, # see below.
        default='something', #default value for this field, for example, "Tien Lee"
        db_column='first_name', #specify this will overwrite the default "first_name"
        db_index=False, #if True, a database index will be created for this field.
        db_tablespace='The name of the database tablespace to use for this field’s index',
        editable=True, # If False, the field will not be displayed in the admin or any other ModelForm. They are also skipped during model validation.
        error_message='',
        help_text='',
        primary_key=False,
        unique=False,
        max_length=30) # max length is for CharField.

    last_name = models.CharField(max_length=30)

    # another example of verbose name;
    middle_name = models.CharField("person's first name", max_length=30) # First position argument is the verbose name.


# Example on Choice:
from django.db import models

class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)
        # student.year_in_school in...

# Relationship
# Many-to-one relationships

from django.db import models

class Manufacturer(models.Model):
    # some attributes and methods.
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...
    pass

# Many-to-many relationships
# ManyToManyField requires a positional argument: the class to which the model is related.

from django.db import models

class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)



# Models across files¶
#
# It’s perfectly OK to relate a model to one from another app. To do this, import the related model at the top of the file where your model is defined. Then, just refer to the other model class wherever needed. For example:

from django.db import models
from geography.models import ZipCode

class Restaurant(models.Model):
    # ...
    zip_code = models.ForeignKey(
        ZipCode,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

class Example(models.Model):
    foo__bar = models.IntegerField() # 'foo__bar' has two underscores!



# Field name restrictions¶
# Django places only two restrictions on model field names:

    # A field name cannot be a Python reserved word, because that would result in a Python syntax error. For example:

class Example(models.Model):
    pass = models.IntegerField() # 'pass' is a reserved word!

    # A field name cannot contain more than one underscore in a row, due to the way Django’s query lookup syntax works. For example:

class Example(models.Model):
    foo__bar = models.IntegerField() # 'foo__bar' has two underscores!




# Meta options¶

# Give your model metadata by using an inner class Meta, like so:

from django.db import models

class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"

# Model metadata is “anything that’s not a field”, such as ordering options (ordering), database table name (db_table), or human-readable singular and plural names (verbose_name and verbose_name_plural). None are required, and adding class Meta to a model is completely optional.
#
# A complete list of all possible Meta options can be found in the model option reference.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#




















