#!/usr/bin/env python
# coding: utf-8

# # Run the cells...

# In[20]:


import sys
from indicnlp import common
from indicnlp.tokenize import sentence_tokenize
from indicnlp.tokenize import indic_tokenize
import gensim
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from indicnlp.tokenize import sentence_tokenize
from indicnlp.tokenize import indic_tokenize 



# The path to the local git repo for Indic NLP library
INDIC_NLP_LIB_HOME=r"indic_nlp_library"

# The path to the local git repo for Indic NLP Resources
INDIC_NLP_RESOURCES=r"indic_nlp_resources"

# Add library to Python path
sys.path.append(r'{}\src'.format(INDIC_NLP_LIB_HOME))

# Set environment variable for resources folder
common.set_resources_path(INDIC_NLP_RESOURCES)


def text_similarity(text1,text2):
    #find the no. of docs in file1
    file_docs = []
    

    
    tokens = sentence_tokenize.sentence_split(text1, lang='mr')
    #tokens = sent_tokenize(f.read())
    for line in tokens:
        file_docs.append(line)

    #print("Number of documents:",len(file_docs))

    #Tokenize each document
    gen_docs = [[w.lower() for w in indic_tokenize.trivial_tokenize(text)] 
                for text in file_docs]

    dictionary = gensim.corpora.Dictionary(gen_docs)
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]

    tf_idf = gensim.models.TfidfModel(corpus)
    #for doc in tf_idf[corpus]:
        #print([[dictionary[id], np.around(freq, decimals=2)] for id, freq in doc])
    
    
    # building the index
    sims = gensim.similarities.Similarity('C:/Users/anike/NLP_mini_project/',tf_idf[corpus], num_features=len(dictionary))

    #file2
    file2_docs = []

   
    tokens = sentence_tokenize.sentence_split(text2, lang='mr')
    #tokens = sent_tokenize(f.read())
    for line in tokens:
            file2_docs.append(line)

    #print("Number of documents:",len(file2_docs))  
    for line in file2_docs:
        query_doc = [w.lower() for w in indic_tokenize.trivial_tokenize(line)]
        query_doc_bow = dictionary.doc2bow(query_doc)
    

    #Similarity


    avg_sims = [] # array of averages

    # for line in query documents
    for line in file2_docs:
            # tokenize words
            query_doc = [w.lower() for w in indic_tokenize.trivial_tokenize(line)]
            # create bag of words
            query_doc_bow = dictionary.doc2bow(query_doc)
            # find similarity for each document
            query_doc_tf_idf = tf_idf[query_doc_bow]
        
            # calculate sum of similarities for each query doc
            sum_of_sims =(np.sum(sims[query_doc_tf_idf], dtype=np.float32))
            # calculate average of similarity for each query doc
            avg = sum_of_sims / len(file_docs)
    
            # add average values into array
            avg_sims.append(avg)  
       # calculate total average
    total_avg = np.sum(avg_sims, dtype=np.float)
        # round the value and multiply by 100 to format it as percentage
    percentage_of_similarity = round(float(total_avg) * 100)
        # if percentage is greater than 100
        # that means documents are almost same
    if percentage_of_similarity >= 100:
        percentage_of_similarity = 100

    return percentage_of_similarity

