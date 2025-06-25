import pandas as pd
import matplotlib.pyplot as plt
import os

def generate():
    if not os.path.exists("results.csv"):
        print("No data available.")
        return

    df = pd.read_csv("results.csv", names=["Name", "Score"])
    df["Score"] = pd.to_numeric(df["Score"], errors='coerce')  # ⬅ ensures numeric type, drops invalid entries
    df = df.dropna(subset=["Score"])  # ⬅ removes any rows where Score is not a number
    df["Score"] = df["Score"].astype(int)

    # 📊 1. Histogram of Score Distribution
    plt.figure(figsize=(6,4))
    df["Score"].plot.hist(bins=range(0,12), rwidth=0.8, color='skyblue', edgecolor='black')
    plt.title("Score Distribution of Students")
    plt.xlabel("Scores")
    plt.ylabel("Number of Students")
    plt.grid(True)
    plt.savefig("static/score_distribution.png")
    plt.close()

    # 📈 2. Bar Chart of Top 5 Scorers
    top_scorers = df.sort_values(by="Score", ascending=False).head(5)
    plt.figure(figsize=(6,4))
    plt.bar(top_scorers["Name"], top_scorers["Score"], color='lightgreen', edgecolor='black')
    plt.title("Top 5 Scorers")
    plt.xlabel("Student Name")
    plt.ylabel("Score")
    plt.savefig("static/top_scorers.png")
    plt.close()
