import praw
import csv

# Authorized Config
reddit = praw.Reddit(
    client_id="hS-ftEhWxwnx4FNccvST-Q",  
    client_secret="c8CJbFeUmT6KDoxwNH4IWsuDhF_lZw", 
    user_agent="Feedback Analysis", 
)

subreddit = reddit.subreddit("technology")

# CSV file setup
csv_filename = "reddit_comments.csv"
max_comments = 2000  # Set the desired number of comments
comment_count = 0

with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Post Title", "Comment", "Label"])  # CSV Header

    print("Fetching latest posts from /r/technology...")
    for post in subreddit.new():  # No limit on posts
        if comment_count >= max_comments:
            break
        
        print(f"Processing post: {post.title}")
        
        # Fetch and process comments
        post.comments.replace_more(limit=0)  # Ignore "more comments"
        for comment in post.comments.list():  # Extract all comments
            if comment_count >= max_comments:
                break
            if comment.body.strip():  # Skip empty comments
                writer.writerow([post.title, comment.body, ""])  # Leave label blank
                comment_count += 1
        
        print(f"Processed {comment_count} comments")

print(f"Data saved to {csv_filename}")