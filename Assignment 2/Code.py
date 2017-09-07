
# coding: utf-8

# # Importing libraries

# In[1]:

import pandas as pd
from nltk.tokenize import RegexpTokenizer
from collections import defaultdict


# # Loading Data and Tokenizers

# In[2]:

data = pd.read_csv('wikipedia-sentences.csv', delimiter='\t', names=['URL', 'Text'])
tokenizer = RegexpTokenizer(r'\w+')
index = defaultdict(list)


# # Preprocessing Functions

# In[3]:

def convert_to_lower(s):
    return s.lower()

def tokenize(s):
    return tokenizer.tokenize(s)


# # Building Inverted Index

# In[8]:

print('Total:', len(data['Text']))
for doc_id, text in enumerate(data['Text'], start=0):
    print(doc_id, end='\r')
    terms = tokenize(convert_to_lower(text))
    for term in set(terms):
        index[term].append(doc_id)


# In[9]:

len(index)


# # Query Functions

# ## Retrieve operation
# __Input__: term <br>
# __Output__: posting list of the term, if exists

# In[10]:

def one_word_query(word):
    return index[word] if word in index else None


# ## AND operation
# __Input__: 2 posting lists<br>
# __Output__: Intersection of the 2 posting lists

# In[11]:

def And(p1, p2):
    result = list()

    i = j = 0
    while i < len(p1) and j < len(p2):
        if p1[i] == p2[j]:
            result.append(p1[i])
            i += 1
            j += 1
        elif p1[i] < p2[j]:
            i += 1
        else:
            j += 1

    return result


# ## AND operation returns top k documents
# __Input__: 2 posting lists, k<br>
# __Output__: Intersection of the 2 posting lists (top k)

# In[12]:

def get_top_k(p1, p2, k):
    result = list()

    i = j = 0
    while i < len(p1) and j < len(p2) and k != 0:
        if p1[i] == p2[j]:
            result.append(p1[i])
            i += 1
            j += 1
            k -= 1
        elif p1[i] < p2[j]:
            i += 1
        else:
            j += 1

    return result


# # Testing

# In[13]:

data['Text'].head()


# In[14]:

query = ['alain', 'connes']


# In[15]:

result1 = And(one_word_query(query[0]), one_word_query(query[1]))


# In[16]:

result1


# In[17]:

result2 = get_top_k(one_word_query(query[0]), one_word_query(query[1]), k=5)


# In[18]:

result2


# # Getting the URLs given doc id

# In[19]:

data.iloc[result2]


# In[ ]:



