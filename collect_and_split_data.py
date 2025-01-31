import pandas as pd
import os
import praw

# Authorized Config
reddit = praw.Reddit(
    client_id="hS-ftEhWxwnx4FNccvST-Q",  
    client_secret="c8CJbFeUmT6KDoxwNH4IWsuDhF_lZw", 
    user_agent="Feedback Analysis", 
)

# focus on the posts in 'technology
subreddit = reddit.subreddit("technology")

# store all the comments
total_comments = []
# according to the calculation, about 2000 comments needed in total
max_comments = 2000
# acutal number of comments we get
comment_count = 0

print("Fetching posts and comments from /r/technology ...... ")
for post in subreddit.new():  # Fetch new posts
    if comment_count >= max_comments:
        break

    # Fetch and process comments
    post.comments.replace_more(limit=0)  # Ignore "more comments"
    for comment in post.comments.list():  # Extract all comments
        if comment_count >= max_comments:
            break
        if comment.body.strip():  # Skip empty comments
            total_comments.append([post.title, comment.body, ""])  # Leave label blank
            comment_count += 1

    print(f"Processed {comment_count} comments")

total_comments_df = pd.DataFrame(total_comments, columns=["Post Title", "Comment", "Label"])

# Select data from the 70th row to the last 
# (Keep the first 70 comments as annotation examples, only label on the remaining comments)
comments_df = total_comments_df.iloc[69:].reset_index(drop=True)

# Shuffle the data randomly
comments_df_shuffled = comments_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Define the number of splits and size per split
num_splits = 8
split_size = 240

total_comments = len(comments_df_shuffled)
duplicate_count = int(0.15 * total_comments)  # 15% of total comments will be duplicated

duplicates = comments_df_shuffled.sample(n=duplicate_count, random_state=42)
comments_df_extended = pd.concat([comments_df_shuffled, duplicates]).sample(frac=1, random_state=42).reset_index(drop=True)

# Ensure the output directory exists
output_dir = "datasets"
os.makedirs(output_dir, exist_ok=True)

# Dictionary to track comment occurrences across files
comment_file_map = {}

print('Spliting data ......')

# Split the data into 8 parts, ensuring no duplicate comments within the same file
split_data = []
for i in range(num_splits):
    start_idx = i * split_size
    end_idx = start_idx + split_size
    subset = comments_df_extended.iloc[start_idx:end_idx].drop_duplicates(subset=["Comment"]).reset_index(drop=True)
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
    output_filename = os.path.join(output_dir, f"dataset_{i+1}.xlsx")
    subset.to_excel(output_filename, index=False)

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
for i, (comment, files) in enumerate(duplicated_comments.items()):
    if i >= 10:
        break

# Print the total number of unique comments
unique_comments = len(comment_file_map)
print(f"Total unique comments: {unique_comments}")

print(f"Data has been split into {num_splits} files with 15% duplication across different files but no duplicates within the same file and saved in '{output_dir}' directory.")
