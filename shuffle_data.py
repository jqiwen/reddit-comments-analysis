import pandas as pd
import os
import random

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

total_comments = len(df_shuffled)
duplicate_count = int(0.15 * total_comments)  # 15% of total comments will be duplicated

duplicates = df_shuffled.sample(n=duplicate_count, random_state=42)
df_extended = pd.concat([df_shuffled, duplicates]).sample(frac=1, random_state=42).reset_index(drop=True)

# Ensure the output directory exists
output_dir = "split_files"
os.makedirs(output_dir, exist_ok=True)

# Dictionary to track comment occurrences across files
comment_file_map = {}

# Split the data into 8 parts, ensuring no duplicate comments within the same file
split_data = []
for i in range(num_splits):
    start_idx = i * split_size
    end_idx = start_idx + split_size
    subset = df_extended.iloc[start_idx:end_idx].drop_duplicates(subset=["Comment"]).reset_index(drop=True)
    split_data.append(subset)

# Ensure that each comment appears in at most two files
final_splits = []
comment_seen = {}
for subset in split_data:
    unique_comments = []
    for _, row in subset.iterrows():
        comment = row["Comment"]
        if comment not in comment_seen:
            comment_seen[comment] = 1
            unique_comments.append(row)
        elif comment_seen[comment] < 2:  # Allow at most two occurrences
            comment_seen[comment] += 1
            unique_comments.append(row)
    final_splits.append(pd.DataFrame(unique_comments))

# Save split files
for i, subset in enumerate(final_splits):
    output_filename = os.path.join(output_dir, f"reddit_comments_part_{i+1}.csv")
    subset.to_csv(output_filename, index=False)

# Print duplicated comments and which files they appear in
comment_file_map = {}
for i, subset in enumerate(final_splits):
    for comment in subset["Comment"].tolist():
        if comment in comment_file_map:
            comment_file_map[comment].append(f"part_{i+1}")
        else:
            comment_file_map[comment] = [f"part_{i+1}"]

# Display only first few duplicates to avoid slow execution
duplicated_comments = {c: f for c, f in comment_file_map.items() if len(f) > 1}
print("Duplicated Comments Across Files (showing first 10):")
for i, (comment, files) in enumerate(duplicated_comments.items()):
    if i >= 10:
        break
    print(f"Comment: {comment}\nAppears in files: {', '.join(files)}\n")

# Print the total number of unique comments
unique_comments = len(comment_file_map)
print(f"Total unique comments: {unique_comments}")

print(f"Data has been split into {num_splits} files with 15% duplication across different files but no duplicates within the same file and saved in '{output_dir}' directory.")
