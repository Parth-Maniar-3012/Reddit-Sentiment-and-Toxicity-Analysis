# 📘 Reddit Sentiment & Toxicity Analysis

Analyze public sentiment and toxicity in Reddit communities using VADER sentiment analysis, keyword-based toxicity detection, and event-based trend tracking. This project helps identify emotional and behavioral patterns in real-time social media data.

---

## 📁 Folder Structure

```
reddit_sentiment_project/
├── data/
│   ├── reddit_combined_10k.csv              # Raw Reddit posts
│   ├── reddit_sentiment.csv                 # Posts with VADER sentiment score + label
│   ├── reddit_with_toxic_flag.csv           # Added toxicity_flag from keyword filter
│   ├── sentiment_over_time.png              # Line chart of sentiment trend
│   ├── sentiment_by_subreddit.png           # Bar chart: sentiment per subreddit
│   ├── top_toxic_words_bar.png              # Most common toxic terms (bar chart)
│   ├── toxicity_distribution_pie.png        # Pie chart of toxic vs non-toxic posts
│   ├── sentiment_vs_toxicity.png            # Boxplot: sentiment vs toxicity
|   ├── wordcloud_positive.png               # Wordcloud: Positivie
|   ├── wordcloud_negative.png               # Wordcloud: Negative
├── scripts/
│   ├── reddit_scraper.py                    # Scrapes top Reddit posts using PRAW
|   ├── sentiment_analysis.py                # Applies VADER sentiment analysis
│   ├── reddit_full_analysis                 # end-to-end analysis of Reddit posts
│   ├── toxicity_detection.py                # Flags posts using toxic wordlist
│   ├── event_analysis.py                    # Tracks sentiment/toxicity over time for keyword
├── presentation/
│   └── Reddit_Sentiment_Analysis_Project.pptx       # Final presentation slides
├── report/
│   └── reddit_sentiment_report.docx         # Project report
```

---

## ▶️ How to Run the Project

> Make sure you have Python 3 and install the required libraries (`pip install -r requirements.txt` or manually).

---

### 🔹 Step 1: Scrape Reddit Posts
```bash
python src/reddit_scraper.py
```
- Scrapes top posts from target subreddits
- Saves to: `data/reddit_combined_10k.csv`

---

### 🔹 Step 2: Perform Sentiment Analysis (VADER)
```bash
python src/sentiment_analysis.py
```
- Adds `vader_score` and `sentiment` (Positive/Neutral/Negative)
- Saves to: `data/reddit_sentiment.csv`

---

### 🔹 Step 3: Detect Toxicity via Keyword Flagging
```bash
python src/toxicity_detection.py
```
- Adds `toxicity_flag` column (1 = toxic, 0 = clean)
- Saves to: `data/reddit_with_toxic_flag.csv`
- Produces charts:
  - Toxic vs Non-toxic (pie)
  - Sentiment vs Toxicity (boxplot)
  - Top toxic words (bar chart)

---

### 🔹 Step 4: Analyze Event-Based Reactions (Optional)
```bash
python src/event_analysis.py
```
- Filter posts by keywords (e.g. “war”, “AI”)  
- Plots emotional + toxic trends over time  
- Output: `event_sentiment_trend_<keyword>.png`

---

## 📊 Output Summary

| Output File                             | Description                                    |
|----------------------------------------|------------------------------------------------|
| `reddit_sentiment.csv`                 | Posts with sentiment labels (VADER)           |
| `reddit_with_toxic_flag.csv`           | Includes toxicity detection                   |
| `sentiment_over_time.png`              | Time series chart of sentiment                |
| `top_toxic_words_bar.png`              | Top toxic words chart                         |
| `toxicity_distribution_pie.png`        | Toxic vs clean post distribution              |
| `sentiment_vs_toxicity.png`            | Boxplot of sentiment vs toxicity              |

---

## 🛠️ Tools & Libraries Used

- `Python 3.x`
- `PRAW` – Reddit scraping
- `VADER SentimentIntensityAnalyzer` – Sentiment labeling
- `matplotlib`, `seaborn` – Data visualization
- `pandas` – Data manipulation
- `collections.Counter` – Word frequency analysis

---

## 📂 Final Deliverables

- ✅ `Reddit_Sentiment_Analysis_Project.pptx` – PowerPoint with all charts & insights
- ✅ `reddit_sentiment_report.docx` – Written report with analysis & findings
