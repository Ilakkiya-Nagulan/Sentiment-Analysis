# Sentiment-Analysis

This repository contains a Streamlit web application for performing sentiment analysis on text input and CSV files.

## Installation

To run this sentiment analysis application, you need to install the following dependencies:

1. **Streamlit**: For building the web app interface.
2. **TextBlob**: For sentiment analysis.
3. **pandas**: For data manipulation and analysis.
4. **clean-text**: For text cleaning.
5. **matplotlib**: For plotting the pie chart.

You can install these dependencies using the following commands:

```bash
pip install streamlit
pip install textblob
pip install pandas
pip install clean-text
pip install matplotlib
```

Additionally, make sure you have the following:

- **Python**: Ensure you have Python installed (version 3.6 or higher).

### Running the Application

1. Clone the repository:

```bash
git clone https://github.com/your-username/Sentiment-Analysis.git
cd Sentiment-Analysis
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

> Note: Make sure to create a `requirements.txt` file that includes all the required packages. You can generate this file using:

```bash
pip freeze > requirements.txt
```

3. Run the Streamlit application:

```bash
streamlit run Sentiment_Analysis.py
```

### Additional Files

Make sure you include the emoji images (`Smiling_Emoji.png`, `Sad_Emoji.png`, `Neutral_Emoji.webp`) in the same directory as your Streamlit app, or provide the correct path to these images in your code.

### Usage

- **Analyze Text**: Enter any text to analyze its sentiment. The sentiment (Positive, Negative, or Neutral) along with its polarity and subjectivity will be displayed. Corresponding emojis will be shown based on the sentiment.
- **Clean Text**: Enter any text to clean it by removing extra spaces, stopwords, converting to lowercase, etc.
- **Analyze CSV**: Upload a CSV file containing text data (ensure there's a column named `tweets`). The sentiment analysis will be performed on the uploaded data, and results will be displayed. You can download the analyzed data as a CSV file and visualize the sentiment distribution using a pie chart.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- [Streamlit](https://www.streamlit.io/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [pandas](https://pandas.pydata.org/)
- [clean-text](https://pypi.org/project/clean-text/)
- [matplotlib](https://matplotlib.org/)
```
