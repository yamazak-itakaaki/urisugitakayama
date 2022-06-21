
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kaiintouroku(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    miyozi = models.TextField(db_column='Miyozi', db_collation='C', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='Name', db_collation='C', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mail = models.TextField(db_column='Mail', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kaiintouroku'


class Room(models.Model):
    room_id = models.IntegerField(db_column='Room_id', primary_key=True)  # Field name made lowercase.
    room_num = models.IntegerField(db_column='Room_num', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room'


class Yoyaku(models.Model):
    yoyaku_id = models.IntegerField(db_column='Yoyaku_id', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    room_id = models.IntegerField(db_column='Room_id', blank=True, null=True)  # Field name made lowercase.
    time = models.IntegerField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'yoyaku'

