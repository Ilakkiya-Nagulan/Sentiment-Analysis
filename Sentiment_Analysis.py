from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext
import matplotlib.pyplot as plt

st.header('Sentiment Analysis')

with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text:
        blob = TextBlob(text)
        st.write('Polarity: ', round(blob.sentiment.polarity, 2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity, 2))
        sentiment = 'Positive' if blob.sentiment.polarity > 0 else 'Negative' if blob.sentiment.polarity < 0 else 'Neutral'
        st.write('Sentiment: ', sentiment)

        # Insert images for positive, negative and neutral sentiment
        if sentiment == 'Positive':
            st.image('Smiling_Emoji.png', width=150)
        elif sentiment == 'Negative':
            st.image('Sad_Emoji.png', width=150)
        elif sentiment == 'Neutral':
            st.image('Neutral_Emoji.webp', width=150)

    pre = st.text_input('Clean Text: ')
    if pre:
        st.write(cleantext.clean(pre, clean_all=False, extra_spaces=True,
                                 stopwords=True, lowercase=True, numbers=True, punct=True))

with st.expander('Analyze CSV'):
    upl = st.file_uploader('Upload file')

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

    if upl:
        df = pd.read_excel(upl)
        
        # Check if the 'Unnamed: 0' column exists before trying to delete it
        if 'Unnamed: 0' in df.columns:
            del df['Unnamed: 0']
        
        df['score'] = df['tweets'].apply(score)
        df['analysis'] = df['score'].apply(analyze)
        st.write(df.head(100))


        csv = df.to_csv(index=False).encode('utf-8')

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='sentiment.csv',
            mime='text/csv',
        )

        positive_count = (df['analysis'] == 'Positive').sum()
        negative_count = (df['analysis'] == 'Negative').sum()
        neutral_count = (df['analysis'] == 'Neutral').sum()
        total_comments = len(df)

        # Display the counts
        st.write(f"Number of Positive Comments: {positive_count}")
        st.write(f"Number of Negative Comments: {negative_count}")
        st.write(f"Number of Neutral Comments: {neutral_count}")
        st.write(f"Total Number of Comments: {total_comments}")


        # Create a pie chart to visualize the sentiment distribution
        fig, ax = plt.subplots(figsize=(5, 5))
        labels = ['Positive', 'Negative', 'Neutral']
        sizes = [positive_count, negative_count, neutral_count]
        colors = ['red', 'yellow', 'green']  # Specify the colors here
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

        st.write('\n\n')

        # Display the pie chart using the `st.pyplot` function
        st.markdown('<div style="text-align:center;font-size:20px;">Sentiment Distribution</div>', unsafe_allow_html=True)
        st.write('\n\n\n\n')
        st.pyplot(fig)