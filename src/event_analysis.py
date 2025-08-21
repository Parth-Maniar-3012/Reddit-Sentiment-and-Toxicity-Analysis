# event_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load Reddit data with sentiment + toxicity
df = pd.read_csv("data/reddit_with_toxic_flag.csv")
df["created"] = pd.to_datetime(df["created"])
df["date"] = df["created"].dt.date

# 🔍 Step 1: Filter for an event by keyword
keyword = "war"  # Change to 'AI', 'inflation', etc.
df_event = df[df["text"].str.contains(keyword, case=False, na=False)]

# Optional: Limit to specific time period
# df_event = df_event[(df_event["date"] >= pd.to_datetime("2024-03-01")) & (df_event["date"] <= pd.to_datetime("2024-03-15"))]

# 🔢 Step 2: Group by date for average sentiment & toxicity
daily_avg = df_event.groupby("date")[["vader_score", "toxicity_flag"]].mean().reset_index()

# 📊 Step 3: Plot sentiment and toxicity over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=daily_avg, x="date", y="vader_score", marker="o", label="Sentiment")
sns.lineplot(data=daily_avg, x="date", y="toxicity_flag", marker="x", label="Toxicity (0–1)")
plt.axhline(0, linestyle="--", color="gray")
plt.title(f"Sentiment & Toxicity Trend: Posts mentioning '{keyword}'")
plt.xlabel("Date")
plt.ylabel("Score")
plt.legend()
plt.tight_layout()

# Save chart
os.makedirs("data", exist_ok=True)
plt.savefig(f"data/event_sentiment_trend_{keyword}.png")
plt.close()

print(f"✅ Event analysis complete. Chart saved to: data/event_sentiment_trend_{keyword}.png")
