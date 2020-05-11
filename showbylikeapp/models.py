from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Posts(models.Model):
	
   txt_description =models.TextField(blank=True,null=True)
   fk_user = models.ForeignKey(User,on_delete = models.DO_NOTHING,blank= True,null=True)
   txt_tags = models.TextField(blank=True,null=True)
   
class Images(models.Model):
   txt_file_name = models.TextField(blank=True,null=True)
   fk_posts = models.ForeignKey(Posts,on_delete=models.DO_NOTHING)
   
  
class Tags(models.Model):
	chr_tag = models.CharField(max_length=20,blank=True,null=True)
	chr_tag2 = models.CharField(max_length=20,blank=True,null=True)
	int_weight = models.FloatField(blank=True,null=True)
	
	
class Likes(models.Model):
	int_like = models.IntegerField(default=1)
	fk_user =models.ForeignKey(User,on_delete=models.DO_NOTHING)
	fk_posts =models.ForeignKey(Posts,on_delete = models.DO_NOTHING)
	