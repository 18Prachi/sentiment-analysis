# 🧠 Sentiment Analysis App

A simple and interactive web app built with **Streamlit** that performs sentiment analysis using **TextBlob**. You can analyze individual text input or bulk content via CSV upload.

🌐 **Live App**: [sentiment-analysis-101.streamlit.app](https://sentiment-analysis-101.streamlit.app/)

---

## 🔍 Features

- ✍️ Analyze sentiment of manually entered text
- 📁 Upload CSV files for batch sentiment analysis
- 🧹 Clean text (remove punctuation, numbers, stopwords, etc.)
- 📊 View polarity and subjectivity scores
- 📥 Download the processed CSV with results

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/18Prachi/sentiment-analysis.git
cd sentiment-analysis
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run main.py
```
---
## 📄 CSV Format

Your uploaded CSV must include a column named `Text` containing the text to be analyzed.

---
## 🛠 Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [Pandas](https://pandas.pydata.org/)
- [clean-text](https://pypi.org/project/clean-text/)

---
Made with ❤️ using Python & Streamlit

