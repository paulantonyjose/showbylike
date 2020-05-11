from showbylikeapp.models import *

tags_list= Posts.objects.values_list('txt_tags',flat=True)
sep_tag_list=[]
for tag_string in tags_list:
	for tag in tag_string.split(','):
		if tag:
			if len(tag.split(' '))>=2:
			    pass
			elif tag[0]==' ':
				sep_tag_list.append(tag[1:].lower())
			else:
				sep_tag_list.append(tag.lower())
f=open('tags.csv','w')
k=''
for w1 in sep_tag_list:
	for w2 in sep_tag_list:
		k=k+w1+'\t'+w2+'\n'
f.write(k)

f.close()
