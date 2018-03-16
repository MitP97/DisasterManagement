# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# Table Shelter: id, total capacity of people, capacity used, Food packets needed, first aid packets needed

# Table Civilians: all biodata, family ID etc
# Table Users : all bio data, access level
# Table Supplier logs: id, name, quantity supplied, type(food, first aid etc)
# Table Current stock: current food packets, current first aid packets


SHELTER_TYPE_CHOICES =(
    ('g','government'),
    ('a','ad-hoc'),
)

GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female'),
    ('o', 'Other'),
)

ROLE_CHOICES = (
    ('a', 'Admin'),
    ('o', 'Operator'),
    ('s', 'Supplier'),
)

SUPPLY_TYPE_CHOICES = (
    ('fp','food_packet'),
    ('fa','first_aid'),
    ('b','beddings'),
    ('w','water'),
)

class Shelter(models.Model):
    total_capacity_of_people = models.IntegerField()
    capacity_used =  models.IntegerField()
    food_packets_needed = models.IntegerField()
    first_aid_packets_needed = models.IntegerField()
    shelter_latitude = models.DecimalField(max_digits=9,decimal_places=6)
    shelter_longitude = models.DecimalField(max_digits=9,decimal_places=6)
    shelter_type = models.CharField(max_length=10,choices = SHELTER_TYPE_CHOICES)


class CurrentStock(models.Model):
    current_stock = models.ForeignKey(Shelter)
    food_packets_available = models.IntegerField()
    first_aid_packets_available = models.IntegerField()
    bedding_packets_available = models.IntegerField()
    water_available = models.IntegerField()

class SystemUsers(AbstractUser):
    shelter = models.ForeignKey(Shelter)
    contact = models.IntegerField()
    dob = models.CharField()
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100 , blank = True , null = True)
    address_line_3 = models.CharField(max_length=100 , blank = True , null = True)
    gender = models.CharField(max_length=10, choices = GENDER_CHOICES)
    aadhar_number = models.IntegerField()
    user_role = models.CharField(max_length=10, choices = ROLE_CHOICES)

class Families(models.Model):
    head_name = models.CharField(max_length=100 )
    number_of_members = models.IntegerField()
    family_address_line_1 = models.CharField(max_length=100)
    family_address_line_2 = models.CharField(max_length=100 , blank = True , null = True)
    family_address_line_3 = models.CharField(max_length=100 , blank = True , null = True)

    # def create(self,post):
    #     self.last_name = post.get('last_name')
    #     self.number_of_members = post.get('number_of_members')
    #     self.save()

class Civilians(models.Model):
    family = models.ForeignKey(Families)
    current_shelter = models.ForeignKey(Shelter, related_name='current_shelter', null = True, blank = True)
    allocated_shelter = models.ForeignKey(Shelter, related_name='allocated_shelter', null = True, blank = True)
    first_name = models.CharField(max_length=100 )
    middle_name = models.CharField(max_length=100 )
    last_name = models.CharField(max_length=100 )
    contact = models.IntegerField()
    dob = models.CharField()
    email = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank = True, null = True)
    address_line_3 = models.CharField(max_length=100, blank = True, null = True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.IntegerField()
    gender = models.CharField(max_length=10,choices = GENDER_CHOICES)
    aadhar_number = models.IntegerField()
    blood_group = models.CharField(max_length=100)
    parent_gaurdian = models.CharField(max_length=100) #DOUBT shouldnt this be a foreignkey and null allowed

    def create(self,post):
        self.family = Families().objects.get(id=post.get('family_id'))
        self.first_name = post.get('first_name')
        self.last_name = post.get('last_name')
        self.contact = post.get('contact')
        self.email = post.get('email')
        self.address_line_1 = post.get('address_line_1')
        if post.get('address_line_2') is not None:
            self.address_line_2 = post.get('address_line_2')
        if post.get('address_line_3') is not None:
            self.address_line_3 = post.get('address_line_3')
        self.city = post.get('city')
        self.state = post.get('state')
        self.country = post.get('country')
        self.pincode = post.get('pincode')
        self.gender = post.get('gender')
        self.aadhar_number = post.get('aadhar_number')
        self.blood_group = post.get('blood_group')
        self.parent_gaurdian = post.get('parent_gaurdian')
        self.save()


class SupplierLogs(models.Model):
    supplier = models.ForeignKey(SystemUsers)
    quantity_supplied = models.IntegerField()
    supply_type = models.CharField(max_length=10, choices = SUPPLY_TYPE_CHOICES)
