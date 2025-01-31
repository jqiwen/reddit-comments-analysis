## **Data Source**
- **Platform:** [Reddit](https://www.reddit.com/)
- **Subreddit:** [r/technology](https://www.reddit.com/r/technology/)
- **API Used:** [PRAW (Python Reddit API Wrapper)](https://praw.readthedocs.io/en/latest/)
- **Collection Method:** Using a Python script that fetches the latest comments from posts.


## **Collection Procedure**
The dataset was collected using the following process:
1. Register a Reddit account and create an application at [Reddit App](https://www.reddit.com/prefs/apps)
2. save your API credentials: `client_id`, `client_secret`, `user_agent`
3. Set up PRAW's praw.Reddit() to connect to the Reddit API.
4. Use the subreddit.new() method to retrieve the latest posts.
5. Fetched up to **2000 comments** from recent posts.
6. Excluded comments that were **empty** or contained only whitespace.
7. Stored each comment along with the **post title** it belongs to.
8. Saved the data in `excel` format.

## **Data Format**
Each row in the dataset represents **one Reddit comment**, and the dataset contains the following columns:

| Column Name | Description |
|------------|------------|
| **Post Title** | The title of the Reddit post where the comment was made |
| **Comment**    | The actual Reddit comment text |
| **Label**      | Initially blank; to be manually annotated |


## Data Processing

There are **2000** comments in total, and **1676** of them are unique

1. **Filtering**: Removed the first **70 rows** (keeping them as examples).
2. **Shuffling**: The dataset was randomly shuffled (`random_state=42`) to ensure a diverse sample.
3. **Splitting**: The dataset was split into **8 CSV files** evenly.
4. **Duplicate Handling**:
   - **15% of comments** were duplicated across different files.
   - **No duplicate comments exist within the same file**.


## Estimated Labeling Time

To estimate how long it would take to label the dataset, our team labeled **10 comments each**, and the average time per comment was recorded.

| Annotator | Comments Labeled | Total Time (minutes) | Avg Time per Comment (seconds) |
|-----------|-----------------|----------------------|--------------------------------|
| **Chenrui Hao** | 10 | 2 min 50 s | 17 sec |
| **Yunze Li** | 10 | 2 min 30s | 15 sec |
| **Qiwen Jiao** | 10 | 2 min 11 sec | 13 sec |

## **Estimated Total Time for Labeling Entire Dataset**
- Average time per comment: **15 seconds**
- Total comments: **1930**
- Estimated total time: **(1930 × 15 seconds) / 3600 seconds** ≈ `8` hours



