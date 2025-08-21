import praw
import pandas as pd
import os
import time

# Reddit API credentials
reddit = praw.Reddit(
    client_id="MDjIJo7rLrONiU89AJQnAg",
    client_secret="uGHk6uOjDxTBrgFC3UKVqg8W0-rN4A",
    user_agent="data-mining-II-bot/0.1 by u/your_reddit_username"
)

# Create data directory if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

TARGET_POSTS = 50000
BATCH_LIMIT = 1000
subreddits = [
    "worldnews",
    "news",
    "politics",
    "AskReddit",
    "technology",
    "Economics",
    "science",
    "TodayILearned",
    "UpliftingNews",
    "explainlikeimfive"
]

all_posts = []

print("🚀 Starting Reddit data collection...")

for name in subreddits:
    print(f"📦 Collecting from r/{name}...")
    subreddit = reddit.subreddit(name)

    for post in subreddit.top(limit=BATCH_LIMIT, time_filter="year"):
        text = post.selftext.strip() if post.selftext else ""
        if not text:
            text = post.title.strip() + " (from title only)"

        all_posts.append({
            "subreddit": name,
            "text":  text,
            "title": post.title,
            "score": post.score,
            "comments": post.num_comments,
            "created": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(post.created_utc)),
            "url": post.url
        })

        if len(all_posts) >= TARGET_POSTS:
            break
    if len(all_posts) >= TARGET_POSTS:
        break

# Save to CSV
df = pd.DataFrame(all_posts)
df.to_csv("data/reddit_combined_10k.csv", index=False)
print(f"✅ Collected {len(df)} posts → data/reddit_combined_10k.csv")