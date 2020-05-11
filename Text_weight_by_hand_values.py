try:
	from showbylikeapp.models import *
	tag_f=open('tags2.csv','r')
	Tags.objects.filter().delete()
	for line in tag_f:
		tag_list=line.replace('  ',' ').split(' ')
		Tags.objects.create(chr_tag=tag_list[0],chr_tag2=tag_list[1],int_weight=float(tag_list[2].replace('\n','')))
except Exception as e:
	import pdb;pdb.set_trace()