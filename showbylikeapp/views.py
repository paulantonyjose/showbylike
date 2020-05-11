from django.shortcuts import render


from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import CharField, Value 
from django.db.models.functions import Concat
from django.db.models import Count,Case,When,IntegerField
from .models import *

from rest_framework import viewsets

from .serializer import FinalSerializer
hostname='https://domainnamehere.com'


# Create your views here.
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination


class ShowByLikeViewSet(viewsets.ViewSet):
    """Lists according to the similarity of a post according to the posts a user has liked.\n
    	A dozen tags have been inserted in the database and each tag has a corresponding row with every other tag along with an integer value from 0 to 1 signifying how similar the two tags are like to each other. More weight will mean more similarity.\n
    	 Ive tried to compute similarity using an nlp library called gensim by training a twitter dataset but there might be incompatibility issues with my android device, so ive inserted them by hand to a text file and inserted with a script.\n
    	 The weight of each post is calculated according to the tags inside them and is sorted according to that weight. \nFormula for weight of a post:\n
    	 Sum of all weights of the tags of that post in relation to the tags of the user liked posts minus the sum of all weights of the tags of the post in relation to the tags of the user disliked posts. \n
    	 API for the post request is used for liking and disliking multiple posts.\n
    		Formatting : {"likes":[1,2,3],"dislikes":[5,6,7]}\n
    		Where 1,2 upto 7 are ids of Post
    	"""
    permission_classes = [IsAuthenticated]

    def list(self, request):
    
    	if not request.user.is_anonymous:
	    	paginator = PageNumberPagination()
	    	paginator.page_size = 5
	    	lst_user_posts=Likes.objects.filter(fk_user=request.user).values('fk_posts__txt_tags','int_like','fk_posts')
	    	qry_liked_all= Likes.objects.values('fk_posts').annotate(int_likes=Count(Case(When(int_like=1, then=1),output_field=IntegerField())),int_dislikes=Count(Case(When(int_like=0, then=1),output_field=IntegerField(),))).values('int_likes','int_dislikes','fk_posts_id')
	    	lst_liked_tags=[]
	    	lst_disliked_tags=[]
	    	for data in lst_user_posts:
	    		if data['int_like']==1:
	    			lst_liked_tags.extend(data['fk_posts__txt_tags'].upper().split(','))
	    		else:
	    			lst_disliked_tags.extend(data['fk_posts__txt_tags'].upper().split(','))
	    	qry_images=Images.objects.annotate(txt_image_path=Concat(Value(hostname),Value('/'),'txt_file_name')).values('txt_image_path','fk_posts_id')
	    	lst_master=list(Posts.objects.values())
	    	qry_tags = Tags.objects.values()
	    	dct_tags= {(data['chr_tag'].upper() +data['chr_tag2']).upper():data['int_weight'] for data in qry_tags}
	    	for post in lst_master:
	    		lst_post_tag=post['txt_tags'].upper().split(',')
	    		weight =0
	    		for tag in lst_post_tag:
	    			for like_tag in lst_liked_tags:
	    				weight +=dct_tags[tag+like_tag]
	    		for tag in lst_post_tag:
	    			for dislike_tag in lst_disliked_tags:
	    				weight -=dct_tags[tag+dislike_tag]
	    		post['weight']=weight
	    		post['lst_images']=qry_images.filter(fk_posts_id=post['id']).values_list('txt_image_path',flat=True)
	    		if lst_user_posts.filter(fk_posts_id=post['id']):
	    			post['chr_status']='Like'
	    			post['weight']= weight+10 if  lst_user_posts.filter(int_like=1,fk_posts_id=post['id']) else weight-10
	    		else:
	    			post['chr_status']= 'Dislike'
	    		post['int_likes'] =qry_liked_all.filter(fk_posts_id=post['id']).first()
	    		post['int_likes'] = 0 if not post['int_likes'] else post['int_likes']['int_likes'] 
	    		post['int_dislikes'] =qry_liked_all.filter(fk_posts_id=post['id']).first()
	    		post['int_dislikes'] = 0 if not post['int_dislikes'] else post['int_dislikes']['int_dislikes']
	    	lst_master= sorted(lst_master,reverse=True, key=lambda k: k['weight'])
	    	lst_master = paginator.paginate_queryset(lst_master, request)
	    	serializer = FinalSerializer(lst_master, many=True)
	    		
	    		#queryset= Posts.objects.all()
	    	return paginator.get_paginated_response(serializer.data)
	    		
	  
	    	return Response('Authentication not provided')
	    	
    def create(self, request,action='Like/Dislike API'):
    		
    		     
	    	lst_likes=request.data.get('likes') or []
	    	lst_already_liked=Likes.objects.filter(fk_user=request.user,int_like=1).values_list('fk_posts_id',flat=True)
	    	list_likes=[like for like in lst_likes if like not in lst_already_liked]
	    	lst_dislikes=request.data.get('dislikes') or []
	    	lst_already_disliked=Likes.objects.filter(fk_user=request.user,int_like=0).values_list('fk_posts_id',flat=True)
	    	lst_dislikes=[like for dislike in lst_dislikes if like not in lst_already_disliked]
	    	lst_likes_all=[]
	    	
	    	for post_id in lst_likes:
	    		ins_like=Likes(fk_user=request.user,fk_posts_id=post_id,int_like=1)
	    		lst_likes_all.append(ins_like)
	    	for post_id in lst_dislikes:
	    		ins_like=Likes(fk_user=request.user,fk_posts_id=post_id,int_like=0)
	    		lst_likes_all.append(ins_like)
	    	Likes.objects.bulk_create(lst_likes_all)
	    	
	    	
	    	
	    	return Response('Thanks for your responses')
		
			





	

	     
	        	
	    	
	   
    