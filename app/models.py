from django.db import models
from rest_framework import serializers
# from django.contrib.auth.models import User
# Create your models here.
class TourGuide(models.Model):
    MALE = 'm'
    FEMALE = 'f'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    id = models.AutoField(primary_key=True)
    #user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='username')
    oneliner = models.CharField(max_length=100, default='no tour details')
    aboutme = models.CharField(max_length=500, default='no about me')
    image = models.CharField(max_length=150, default='english')
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES, default=MALE)
#this is the serializer for the contact model, it explains what fields should be included into the json
class TourGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourGuide
        fields = ('id','name','oneliner','image','gender')
        
class Tour(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    tour_summary = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    guests = models.IntegerField()
    image = models.CharField(max_length=150, default='english')
    category = models.CharField(max_length= 30, default='other category')
    tour_guide = models.ForeignKey(TourGuide, on_delete=models.CASCADE, default='13')
    
class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ('tour_guide_id','title','tour_summary','image','cost','category', 'guests')

# class SingleTourGuide(models.Model):
#     MALE = 'm'
#     FEMALE = 'f'
#     GENDER_CHOICES = (
#         (MALE, 'Male'),
#         (FEMALE, 'Female'),
#     )
#     id = models.AutoField(primary_key=True)
#     #user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
#     aboutme = models.CharField(max_length=500, default='I am a tour guide')
#     name = models.CharField(max_length=20, default='username')
#     oneliner = models.CharField(max_length=100, default='no tour details')
#     image = models.CharField(max_length=150, default='english')
#     gender = models.CharField(max_length=1,choices=GENDER_CHOICES, default=MALE)
#     title = models.CharField(max_length=30)
#     tour_summary = models.CharField(max_length=100)
#     cost = models.DecimalField(max_digits=5, decimal_places=2)
#     guests = models.IntegerField()
#     category = models.CharField(max_length= 30, default='other category')
#     tour_guide = models.ForeignKey(TourGuide, on_delete=models.CASCADE)
    
# class SingleTourGuideSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tour
#         fields = ('oneliner', 'gender','title','tour_summary','image','cost','category', 'guests', 'aboutme', 'name', )        