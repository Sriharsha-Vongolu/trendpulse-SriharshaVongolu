# Task 3 - Analysis with Pandas and NumPy

import pandas as pd
import numpy as np

def main():
    input_file = "data/trends_clean.csv"

    # load csv
    df = pd.read_csv(input_file)

    print(f"Loaded data: {df.shape}")

    # first 5 rows
    print("\nFirst 5 rows:")
    print(df.head())

    # average values
    avg_score = df["score"].mean()
    avg_comments = df["num_comments"].mean()

    print(f"\nAverage score   : {avg_score:.2f}")
    print(f"Average comments: {avg_comments:.2f}")

    # numpy stats
    scores = df["score"].values

    print("\n--- NumPy Stats ---")
    print("Mean score   :", np.mean(scores))
    print("Median score :", np.median(scores))
    print("Std deviation:", np.std(scores))
    print("Max score    :", np.max(scores))
    print("Min score    :", np.min(scores))

    # category with most stories
    most_category = df["category"].value_counts().idxmax()
    count = df["category"].value_counts().max()
    print(f"\nMost stories in: {most_category} ({count} stories)")

    # most commented story
    idx = df["num_comments"].idxmax()
    title = df.loc[idx, "title"]
    comments = df.loc[idx, "num_comments"]
    print(f'\nMost commented story: "{title}" — {comments} comments')

    # add engagement column
    df["engagement"] = df["num_comments"] / (df["score"] + 1)

    # add is_popular column
    df["is_popular"] = df["score"] > avg_score

    # save csv
    output_file = "data/trends_analysed.csv"
    df.to_csv(output_file, index=False)

    print(f"\nSaved to {output_file}")


if __name__ == "__main__":
    main()