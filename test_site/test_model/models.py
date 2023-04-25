from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    instrument = models.CharField(max_length=200)

class Person(models.Model):
    name = models.CharField(max_length =100) 
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField( null=True , blank=True )
    image = models.ImageField()
    file = models.FileField()
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()

class car(models.Model):
    name1 = models.CharField(max_length=100)
    speed = models.IntegerField()
    
    ## It is used only to simplify the user's understanding of the object name that is returned by these models.
    ## It is not a mandatory stack

    def __str__(self):
        return self.name1
    
    class Meta:  
        db_table = "car"  


# The Commands
"""
There are several commands which you will use to interact with migrations and Django’s handling of database schema:

1) migrate         --    which is responsible for applying and unapplying migrations.
2) makemigrations  --    which is responsible for creating new migrations based on the changes you have made to your models.
3) sqlmigrate      --    which displays the SQL statements for a migration.
4) showmigrations  --    which lists a project’s migrations and their status.

"""

"""
AutoField	       --    It is an IntegerField that automatically increments.
BigAutoField       --    It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.
BigIntegerField	   --    It is a 64-bit integer, much like an IntegerField except that it is guaranteed to fit numbers from -9223372036854775808 to 9223372036854775807.
BinaryField	       --    A field to store raw binary data. 
BooleanField	   --    A true/false field. 

"""
# The default form widget for this field is a CheckboxInput.

"""
CharField                 --    A field to store text-based values.
DateField	              --    A date, represented in Python by a datetime.date instance
DateTimeField             --    It is used for date and time, represented in Python by a datetime.datetime instance.
DecimalField              --    It is a fixed-precision decimal number, represented in Python by a Decimal instance.
DurationField	          --    A field for storing periods of time.
EmailField                --    It is a CharField that checks that the value is a valid email address.
FileField                 --    It is a file-upload field.
FloatField	              --    It is a floating-point number represented in Python by a float instance.
ImageField                --    It inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
IntegerField	          --    It is an integer field. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.
GenericIPAddressField     --    An IPv4 or IPv6 address, in string format (e.g. 192.0.2.30 or 2a02:42fe::4).
NullBooleanField          --    Like a BooleanField, but allows NULL as one of the options.
PositiveIntegerField      --    Like an IntegerField, but must be either positive or zero (0).
SlugField                 -- 	Slug is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.
SmallIntegerField	      --    It is like an IntegerField, but only allows values under a certain (database-dependent) point.
TextField                 --	A large text field. The default form widget for this field is a Textarea.
TimeField	              --    A time, represented in Python by a datetime.time instance.
URLField                  --	A CharField for a URL, validated by URLValidator.
UUIDField	              --    A field for storing universally unique identifiers. Uses Python’s UUID class. When used on PostgreSQL, this stores in a uuid datatype, otherwise in a char(32).
PositiveSmallIntegerField --    Like a PositiveIntegerField, but only allows values under a certain (database-dependent) point.

"""

# Relationship Fields
## Django also defines a set of fields that represent relations.

# Field Name	

"""
Description

ForeignKey            -- 	 A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.
ManyToManyField	      --     A many-to-many relationship. Requires a positional argument: the class to which the model is related, which works exactly the same as it does for ForeignKey, including recursive and lazy relationships.
OneToOneField	      --     A one-to-one relationship. Conceptually, this is similar to a ForeignKey with unique=True, but the “reverse” side of the relation will directly return a single object.

"""