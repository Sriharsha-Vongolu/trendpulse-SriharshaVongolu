# Task 2 - Clean data and save as CSV

import pandas as pd
import json
import os

def main():
    # file path (use your generated json file)
    input_file = "data/trends_20260414.json"
    
    print(f"Loading data from {input_file}")

    # load json
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # convert to dataframe
    df = pd.DataFrame(data)

    print(f"\nLoaded {len(df)} stories")

    # remove duplicates
    df = df.drop_duplicates(subset=["post_id"])
    print(f"After removing duplicates: {len(df)}")

    # remove missing values
    df = df.dropna(subset=["post_id", "title", "score"])
    print(f"After removing nulls: {len(df)}")

    # convert datatypes
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].astype(int)

    # remove low quality stories
    df = df[df["score"] >= 5]
    print(f"After removing low scores: {len(df)}")

    # strip whitespace
    df["title"] = df["title"].str.strip()

    # save csv
    output_file = "data/trends_clean.csv"
    df.to_csv(output_file, index=False)

    print(f"\nSaved {len(df)} rows to {output_file}")

    # print category summary
    print("\nStories per category:")
    print(df["category"].value_counts())


if __name__ == "__main__":
    main()