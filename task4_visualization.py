# Task 4 - Visualization

import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    input_file = "data/trends_analysed.csv"

    # load data
    df = pd.read_csv(input_file)

    # create outputs folder
    os.makedirs("outputs", exist_ok=True)

   # Chart 1 - Top 10 Stories
    top10 = df.sort_values("score", ascending=False).head(10)

    # shorten titles
    titles = [t[:50] + "..." if len(t) > 50 else t for t in top10["title"]]

    plt.figure(figsize=(10,6))
    plt.barh(titles, top10["score"])
    plt.xlabel("Score")
    plt.ylabel("Story Title")
    plt.title("Top 10 Stories by Score")
    plt.gca().invert_yaxis()

    plt.tight_layout()
    plt.savefig("outputs/chart1_top_stories.png")
    plt.close()

    # -------------------------------
    # Chart 2 - Stories per Category
    # -------------------------------
    counts = df["category"].value_counts()

    plt.figure(figsize=(8,5))
    plt.bar(counts.index, counts.values)
    plt.xlabel("Category")
    plt.ylabel("Number of Stories")
    plt.title("Stories per Category")

    plt.tight_layout()
    plt.savefig("outputs/chart2_categories.png")
    plt.close()

    # -------------------------------
    # Chart 3 - Scatter Plot
    # -------------------------------
    popular = df[df["is_popular"] == True]
    not_popular = df[df["is_popular"] == False]

    plt.figure(figsize=(8,5))
    plt.scatter(popular["score"], popular["num_comments"], label="Popular")
    plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

    plt.xlabel("Score")
    plt.ylabel("Number of Comments")
    plt.title("Score vs Comments")
    plt.legend()

    plt.tight_layout()
    plt.savefig("outputs/chart3_scatter.png")
    plt.close()

    # -------------------------------
    # Dashboard (Bonus)
    # -------------------------------
    fig, axes = plt.subplots(1, 3, figsize=(18,5))
    fig.suptitle("TrendPulse Dashboard")

    # chart 1
    axes[0].barh(titles, top10["score"])
    axes[0].set_title("Top Stories")
    axes[0].invert_yaxis()

    # chart 2
    axes[1].bar(counts.index, counts.values)
    axes[1].set_title("Categories")

    # chart 3
    axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
    axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
    axes[2].set_title("Score vs Comments")

    plt.tight_layout()
    plt.savefig("outputs/dashboard.png")
    plt.close()

    print("Charts saved in outputs/ folder")


if __name__ == "__main__":
    main()