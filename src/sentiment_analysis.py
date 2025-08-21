import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output folder if needed
os.makedirs("data", exist_ok=True)

# Load Reddit data
df = pd.read_csv("data/reddit_combined_10k.csv")

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()
df["vader_score"] = df["text"].apply(lambda x: analyzer.polarity_scores(str(x))["compound"])

# Label sentiment
def classify(score):
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

df["sentiment"] = df["vader_score"].apply(classify)

# Save sentiment results
df.to_csv("data/reddit_sentiment.csv", index=False)
print("✅ Sentiment data saved to data/reddit_sentiment.csv")

# Plot sentiment distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="sentiment", palette="pastel")
plt.title("Reddit Sentiment Distribution")
plt.ylabel("Post Count")
plt.xlabel("Sentiment")
plt.tight_layout()
plt.savefig("data/sentiment_distribution.png")
plt.show()
