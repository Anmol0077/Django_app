from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class MutualFunds(models.Model):
    mf_id = models.CharField(max_length=60, primary_key=True) 
    mf_name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class CompaniesName(models.Model):
    cp_id = models.CharField(max_length=60,primary_key=True)
    cp_name = models.CharField(max_length=60)
    def __str__(self):
        return self.name        

class Matchingfield(models.Model):
    cp_id = models.CharField(max_length=60)
    mf_id = models.CharField(max_length=60)
    def __str__(self):
        return self.name               

class JoinTableModel(models.Model):
    cp_name = models.CharField(max_length=60)
    mf_name = models.CharField(max_length=60)
    cp_id = models.CharField(max_length=60)
    mf_id = models.CharField(max_length=60)