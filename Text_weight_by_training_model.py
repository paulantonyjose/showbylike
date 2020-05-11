from gensim.models.word2vec import Word2Vec
import gensim.downloader as api
from showbylikeapp.models import *
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors
#import pdb;pdb.set_trace()
# this loads the text8 dataset
#corpus = api.load('text8')

# train a Word2Vec model
#model_text8 = Word2Vec(corpus,iter=10,size=150, window=10, min_count=2, workers=10)  
#model_text8.save('text8')

model_twitter=model = api.load("glove-twitter-25")
fname = get_tmpfile("vectors.kv")
model_twitter.save(fname)
model_twitter = KeyedVectors.load(fname, mmap='r')
Tags.objects.filter().delete()
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
				
from gensim.test.utils import datapath
model_twitter.wv.evaluate_word_pairs(datapath('tags.csv'))
		
#Tags.objects.create(chr_tag=w1,chr_tag2=w2,int_weight=int_similarity)