import praw

# Authorized Config
reddit = praw.Reddit(
    client_id="hS-ftEhWxwnx4FNccvST-Q",  
    client_secret="c8CJbFeUmT6KDoxwNH4IWsuDhF_lZw", 
    user_agent="Feedback Analysis", 
)


subreddit = reddit.subreddit("technology")

print("Fetching latest posts from /r/technology...")
for post in subreddit.new(limit=5): 
    print(f"Title: {post.title}")
    print(f"ID: {post.id}")
    print(f"Reddit Link: https://www.reddit.com{post.permalink}")
    print(f"URL: {post.url}")
    print(f"Score: {post.score}")
    print("-" * 50)

    # 获取每条帖子的评论
    print("Fetching comments for this post...")
    post.comments.replace_more(limit=0)  # 忽略 "更多评论"
    for comment in post.comments.list()[:5]:  # 获取最多 5 条评论
        print(f"Comment: {comment.body}")
        print("-" * 30)
