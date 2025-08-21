# reddit_full_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer

# 📁 Ensure folders exist
os.makedirs("data", exist_ok=True)

# 📥 Load the scraped Reddit dataset
df = pd.read_csv("data/reddit_combined_10k.csv")

# 🧠 Apply VADER Sentiment
analyzer = SentimentIntensityAnalyzer()
df["vader_score"] = df["text"].apply(lambda x: analyzer.polarity_scores(str(x))["compound"])

# 🏷️ Classify sentiment labels
def classify(score):
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

df["sentiment"] = df["vader_score"].apply(classify)
df["date"] = pd.to_datetime(df["created"]).dt.date
df["length"] = df["text"].apply(len)

# ✅ Save updated data
df.to_csv("data/reddit_sentiment.csv", index=False)

# 📊 1. Sentiment by Subreddit
plt.figure(figsize=(10, 6))
sns.barplot(data=df.groupby("subreddit")["vader_score"].mean().reset_index(), 
            x="vader_score", y="subreddit", palette="coolwarm")
plt.title("Average Sentiment by Subreddit")
plt.tight_layout()
plt.savefig("data/sentiment_by_subreddit.png")
plt.close()

# 📌 2. Top 5 Positive and Negative Posts
top_positive = df.sort_values("vader_score", ascending=False).head(5)
top_negative = df.sort_values("vader_score").head(5)
pd.concat([top_positive, top_negative]).to_csv("data/top_sentiment_posts.csv", index=False)

# ☁️ 3. Word Cloud (Positive & Negative)
positive_text = ' '.join(df[df['sentiment'] == 'Positive']["text"].dropna().astype(str))
negative_text = ' '.join(df[df['sentiment'] == 'Negative']["text"].dropna().astype(str))

WordCloud(width=800, height=400, background_color='white').generate(positive_text)\
    .to_file("data/wordcloud_positive.png")

WordCloud(width=800, height=400, background_color='black').generate(negative_text)\
    .to_file("data/wordcloud_negative.png")

# 🕒 4. Sentiment Over Time
daily_avg = df.groupby("date")["vader_score"].mean().reset_index()
plt.figure(figsize=(12, 5))
sns.lineplot(data=daily_avg, x="date", y="vader_score", marker="o")
plt.title("Average Reddit Sentiment Over Time")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("data/sentiment_over_time.png")
plt.close()

# 🔍 5. Top Keywords from Negative Posts
vectorizer = TfidfVectorizer(stop_words='english', max_features=20)
neg_text = df[df["sentiment"] == "Negative"]["text"].dropna().astype(str)
tfidf_matrix = vectorizer.fit_transform(neg_text)
keywords = vectorizer.get_feature_names_out()
pd.DataFrame({"Top Negative Keywords": keywords}).to_csv("data/top_negative_keywords.csv", index=False)

# 📏 6. Post Length vs Sentiment
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="length", y="vader_score", alpha=0.3)
plt.title("Post Length vs Sentiment")
plt.tight_layout()
plt.savefig("data/length_vs_sentiment.png")
plt.close()

# 💬 7. Comment Count vs Sentiment
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="comments", y="vader_score", alpha=0.3)
plt.title("Comments vs Sentiment")
plt.tight_layout()
plt.savefig("data/comments_vs_sentiment.png")
plt.close()

print("✅ Analysis complete. All charts and outputs are saved in the /data folder.")
