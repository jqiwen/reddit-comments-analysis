

This dataset contains comments collected from posters under `https://www.reddit.com/r/technology/`. 


### **Data Source**
- **Platform:** [Reddit](https://www.reddit.com/)
- **Subreddit:** [r/technology](https://www.reddit.com/r/technology/)
- **API Used:** [PRAW (Python Reddit API Wrapper)](https://praw.readthedocs.io/en/latest/)
- **Collection Method:** Extracted using a Python script that fetches the latest comments from posts.


### **2️⃣ Collection Procedure**
The dataset was collected using the following process:
1. Queried the **r/technology** subreddit using PRAW’s `subreddit.new()` method.
2. Fetched up to **2000 comments** from recent posts.
3. Excluded comments that were **empty** or contained only whitespace.
4. Stored each comment along with the **post title** it belongs to.
5. Saved the data in structured format (`CSV` and `Excel`).

### **2️⃣ Data Format**
Each row in the dataset represents **one Reddit comment**, and the dataset contains the following columns:

| Column Name | Description |
|------------|------------|
| **Post Title** | The title of the Reddit post where the comment was made |
| **Comment**    | The actual Reddit comment text |
| **Label**      | Initially blank; to be manually annotated |



## 📊 Data Processing

1. **Filtering**: Removed the first **69 rows** (keeping them as examples).
2. **Shuffling**: The dataset was randomly shuffled (`random_state=42`) to ensure a diverse sample.
3. **Splitting**: The dataset was split into **8 CSV files**, each containing **240 comments**.
4. **Duplicate Handling**:
   - **15% of comments** were duplicated across different files.
   - **No duplicate comments exist within the same file**.
5. **Encoding**: Saved in **UTF-8-SIG** format to prevent encoding issues when opening in Excel.


## ⏳ Estimated Labeling Time

To estimate how long it would take to label the dataset, our team labeled **10 comments each**, and the average time per comment was recorded.

| Annotator | Comments Labeled | Total Time (minutes) | Avg Time per Comment (seconds) |
|-----------|-----------------|----------------------|--------------------------------|
| **Person A** | 10 | 5 min | 30 sec |
| **Person B** | 10 | 6 min | 36 sec |
| **Person C** | 10 | 4 min 30 sec | 27 sec |

### **⚡ Estimated Total Time for Labeling Entire Dataset**
- Average time per comment: **~31 seconds**
- Total comments: **[number of comments]**
- Estimated total time: **(total_comments × 31 seconds) / 60 minutes** ≈ `[final estimate]` hours



