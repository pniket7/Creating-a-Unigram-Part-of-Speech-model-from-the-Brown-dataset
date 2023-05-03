#!/usr/bin/env python
# coding: utf-8

# In[70]:


import nltk
from sklearn.model_selection import train_test_split


# In[76]:


# Load the Brown corpus
corpus = nltk.corpus.PlaintextCorpusReader('/home/niket/Music/brown/brown', '.*')


# In[78]:


# Preprocess the data
sentences = corpus.sents()
tagged_sentences = nltk.pos_tag_sents(sentences)


# In[79]:


# Split the data into training and testing sets
train_sentences, test_sentences, train_tagged_sentences, test_tagged_sentences = train_test_split(sentences, tagged_sentences, test_size=0.2)


# In[80]:


# Train the model
unigram_tagger = nltk.tag.UnigramTagger(train_tagged_sentences)
accuracy = unigram_tagger.evaluate(test_tagged_sentences)
print(f"Accuracy: {accuracy:.2%}")


# In[82]:


# Test the model on a sample sentence
sample_sentence = "The horse runs very fast and wins all the races."

# Tokenize the sentence
tokens = nltk.word_tokenize(sample_sentence)

# Tag the tokens using the trained model
tagged_tokens = unigram_tagger.tag(tokens)

# Print the tagged tokens
print(tagged_tokens)


# In[83]:


#POS TAGS

#Noun (NN)
#Verb (VB)
#Adjective (JJ)
#Adverb (RB)
#Pronoun (PRP)
#Preposition (IN)
#Conjunction (CC)
#Determiner (DT)
#Interjection (UH)


# In[ ]:




