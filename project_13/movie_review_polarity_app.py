#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import streamlit as st
import pickle
import re
import spacy

model = pickle.load(open('project_14_spacy_tfidf_lr.pkl', 'rb'))
nlp = spacy.load('en_core_web_sm')
vectorizer = pickle.load(open('project_14_spacy_tfidf_vectorizer.pkl', 'rb'))

def text_preprocessing(text):
    text = ' '.join(re.sub(r"[^a-zA-Z']", ' ', text).lower().split())
    tokens = [token.lemma_ for token in nlp(text)]
    text = vectorizer.transform([' '.join(tokens)])
    
    return text

st.title('Sentiment Analysis on a Movie Review')
st.markdown('**This is an experimental model to classify the polarity of your movie review. The current model has an accuracy of 88.10%**')

st.header('Share Your Thoughs on a Movie!')
movie = st.text_input('Movie Name')
review = st.text_input('My Review')

if st.button('Submit my movie review'):
    preprocessed_review = text_preprocessing(review)
    pred = model.predict(preprocessed_review)
    if pred == 1.0:
        st.text(f'Glad to hear that you enjoyed the movie {movie}! Thanks for sharing your thoughts!')
    else:
        st.write(f'Thank you for your thoughts. Sorry to hear that the movie {movie} didn\'t meet your expectations.')