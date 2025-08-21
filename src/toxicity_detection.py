# toxicity_detection.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import os

# Step 1: Load sentiment-labeled Reddit data
df = pd.read_csv("data/reddit_sentiment.csv")

# Step 2: Define a basic toxicity wordlist
toxic_words = [
    'hate', 'kill', 'stupid', 'racist', 'idiot', 'moron', 'nazi', 'dumb', 'fool', 'douche',
    'retard', 'loser', 'bastard', 'asshole', 'slur', 'trash', 'garbage', 'worthless',
    'ugly', 'disgusting', 'freak', 'scum', 'creep', 'pervert', 'psycho', 'fat', 'dirtbag',
    'junkie', 'abuse', 'rapist', 'sicko', 'twisted', 'hatefully', 'damn', 'hell', 'bitch',
    'slut', 'whore', 'sexist', 'misogynist', 'terrorist', 'criminal', 'evil', 'menace',
    'animal', 'filthy', 'degenerate', 'unwanted', 'reject', 'attack', 'curse', 'threat'
]

# Step 3: Check if post text contains any toxic words
def contains_toxicity(text):
    text = str(text).lower()
    return any(word in text for word in toxic_words)

# Step 4: Apply toxicity flag
df["contains_toxic_word"] = df["text"].apply(contains_toxicity)
df["toxicity_flag"] = df["contains_toxic_word"].astype(int)

# Step 5: Save the new file
output_path = "data/reddit_with_toxic_flag.csv"
os.makedirs("data", exist_ok=True)
df.to_csv(output_path, index=False)

# Done!
print(f"✅ Toxicity detection complete. Output saved to: {output_path}")
print(df["toxicity_flag"].value_counts())


# Load dataset
df = pd.read_csv("data/reddit_with_toxic_flag.csv")

# Chart 1: Pie Chart – Toxic vs Non-Toxic Posts
tox_counts = df["toxicity_flag"].value_counts()
labels = ['Non-Toxic', 'Toxic']
colors = ['#88c999', '#e57373']

plt.figure(figsize=(6, 6))
plt.pie(tox_counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Overall Toxicity Distribution in Reddit Posts")
plt.tight_layout()
plt.savefig("data/toxicity_distribution_pie.png")
plt.show()

# Step 1: Match toxic words per post
def matched_words(text):
    return [word for word in toxic_words if word in str(text).lower()]

df["matched_words"] = df["text"].apply(matched_words)

# Step 2: Flatten and count
flat_words = [word for sublist in df["matched_words"] for word in sublist]
word_counts = Counter(flat_words).most_common(10)

# Step 3: Create DataFrame for plotting
wc_df = pd.DataFrame(word_counts, columns=["word", "count"])

# Step 4: Plot bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x="count", y="word", data=wc_df, palette="Reds_r")
plt.title("Top 10 Most Common Toxic Words")
plt.xlabel("Count")
plt.ylabel("Toxic Word")
plt.tight_layout()

# Save chart
os.makedirs("data", exist_ok=True)
plt.savefig("data/top_toxic_words_bar.png")
plt.show()