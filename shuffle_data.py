import pandas as pd
import random
import os

# Load the CSV file
csv_filename = "reddit_comments.csv"
df = pd.read_csv(csv_filename)

# Select data from the 70th row to the last
df_filtered = df.iloc[69:].reset_index(drop=True)

# Shuffle the data randomly
df_shuffled = df_filtered.sample(frac=1, random_state=42).reset_index(drop=True)

# Define the number of splits and size per split
num_splits = 8
split_size = 240

# Ensure the output directory exists
output_dir = "split_files"
os.makedirs(output_dir, exist_ok=True)

# Split the data into 8 parts, each containing 240 rows
for i in range(num_splits):
    start_idx = i * split_size
    end_idx = start_idx + split_size

    # Extract subset
    subset = df_shuffled.iloc[start_idx:end_idx]

    # Define output filename
    output_filename = os.path.join(output_dir, f"reddit_comments_part_{i+1}.csv")

    # Save subset to CSV
    subset.to_csv(output_filename, index=False)

print(f"Data has been split into {num_splits} files and saved in '{output_dir}' directory.")
