import csv
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ui import page, data_path

page('Cinema Discovery','Explore the catalog and find titles with similar wording.','RECOMMENDATION SYSTEMS')
@st.cache_data
def catalog():
    rows=[]
    for line in data_path('Copyofmovie_titles.csv').read_text(encoding='utf-8',errors='replace').splitlines():
        parts=line.split(',',2)
        if len(parts)==3:
            rows.append(parts)
    df=pd.DataFrame(rows,columns=['Movie ID','Year','Title'])
    df['Year']=pd.to_numeric(df['Year'],errors='coerce')
    return df.dropna(subset=['Year']).reset_index(drop=True)
@st.cache_resource
def index():
    df=catalog()
    matrix=TfidfVectorizer(analyzer='char_wb',ngram_range=(3,5)).fit_transform(df.Title)
    return matrix
df=catalog()
a,b,c=st.columns(3)
a.metric('Catalog titles',f'{len(df):,}')
b.metric('Earliest release',str(int(df.Year.min())))
c.metric('Latest release',str(int(df.Year.max())))
discover,browse,about=st.tabs(['Discover similar titles','Browse the collection','How it works'])
with discover:
    chosen=st.selectbox('Choose a title',df.index,format_func=lambda i:f'{df.loc[i,"Title"]} ({int(df.loc[i,"Year"])})')
    count=st.slider('Number of suggestions',3,12,6)
    if st.button('Find similar titles',type='primary'):
        scores=cosine_similarity(index()[chosen],index()).ravel()
        matches=[i for i in scores.argsort()[::-1] if i!=chosen and scores[i]>0][:count]
        if not matches: st.info('No title-text matches found. Try another film.')
        for i in matches:
            with st.container(border=True):
                left,right=st.columns([4,1])
                left.subheader(df.loc[i,'Title'])
                left.caption(f'Released {int(df.loc[i,"Year"])} · Catalog ID {df.loc[i,"Movie ID"]}')
                right.metric('Text similarity',f'{scores[i]:.2f}')
with browse:
    term=st.text_input('Search the catalog')
    filtered=df[df.Title.str.contains(term,case=False,regex=False)]
    st.dataframe(filtered.head(500),hide_index=True,use_container_width=True)
    st.bar_chart(df.groupby('Year').size().rename('Titles'))
with about:
    st.markdown("""### Two distinct experiments
This app uses character-level TF–IDF and cosine similarity over the included movie-title catalog. Similarity reflects wording, not plot, genre, audience preference, or recommendation quality.

The original notebook explores SVD collaborative filtering. Its ratings dataset is not included, so this deployed app does not claim to run that SVD model. A full collaborative recommender needs the ratings data and a separate evaluation.
""")
