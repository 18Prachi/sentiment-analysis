import pandas as pd
from textblob import TextBlob
import streamlit as st
import cleantext

st.header('Sentiment Analysis')

# Analyze Text
with st.expander('Analyze Text: '):
    text = st.text_input('Text here: ')
    if text:
        blob = TextBlob(text)
        st.write('Polarity: ', round(blob.sentiment.polarity, 2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity, 2))
    
    pre_cleaned_text = st.text_input('Clean Text: ')
    if pre_cleaned_text:
        st.write(cleantext.clean(pre_cleaned_text, clean_all=False, extra_spaces=True, stopwords=True, lowercase=True, numbers=True, punct=True))

# Analyze csv file
with st.expander('Analyze CSV: '):
    csv_file = st.file_uploader('Upload file')

    def score(x):
        blob1 = TextBlob(x)  
        return blob1.sentiment.polarity
    
    def analyze(x):
        if x >= 0.5:
            return 'Positive'
        elif x <= -0.5:
            return 'Negative'
        else:
            return 'Neutral'

    if csv_file:
        df = pd.read_csv(csv_file)
        del df['Unnamed: 0']
        df['score'] = df['Text'].apply(score)
        df['analysis'] = df['score'].apply(analyze)
        st.write(df.head())

        @st.cache_data
        def convert_df(df):
            return df.to_csv().encode('utf-8')
        
        csv = convert_df(df)

        st.download_button(
            label='Download data as CSV',
            data=csv,
            file_name='sentiment.csv',
            mime='text/csv'
        )