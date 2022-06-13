from django.db import models

# Create your models here.
class Hinatazaka46(models.Model):
    miyozi = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    name = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    birthday = models.DateField(blank=True, null=True)
    city = models.TextField(db_column='city', db_collation='C', blank=True, null=True)  # Field renamed because it was a Python reserved word. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'hinatazaka46'