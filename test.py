from facebook_scraper import get_posts, _scraper
import json

# Load headers from JSON file
with open('./mbasicHeaders.json', 'r') as file:
    _scraper.mbasic_headers = json.load(file)

# Scrape posts
for post in get_posts(
    'NintendoAmerica', 
    base_url="https://mbasic.facebook.com", 
    start_url="https://mbasic.facebook.com/NintendoAmerica?v=timeline", 
    pages=1, 
    options={
        "comments": True, 
        "whitelist_methods": [
            'extract_post_url', 'extract_post_id', 'extract_comments', 
            'extract_text', 'extract_time', 'extract_user_id', 
            'extract_username'
        ]
    },
    cookies="cookies.txt"
):
    print('-----------------------------------')
    print("POST:")
    print(f'Post URL: {post["post_url"]}')
    print(f'Post ID: {post["post_id"]}')
    print(f'Post Text: {post["text"]}')
    print(f'Post Time: {post["time"]},  Post Likes: {post["likes"]},  Post Shares: {post["shares"]},  Post Comments: {post["comments"]}')
    print()
    print('COMMENTS:')
    
    # Check if comments are available
    if post['comments_full'] is None:
        print('No comments')
        print()
        continue
    
    comments = post['comments_full']
    for index, comment in enumerate(comments):
        if index % 2 == 0:
            print(f'Comment ID: {comment["comment_id"]}, Comment URL: {comment["comment_url"]}, Commenter Name: {comment["commenter_name"]}, Commenter URL: {comment["commenter_url"]}, Time: {comment["comment_time"]}')
            print(comment["comment_text"])
            print('REPLIES:')
            for reply_index, reply in enumerate(comment["replies"]):
                if reply_index % 2 == 0:
                    print(f'Replier Name: {reply["commenter_name"]}, Time: {reply["comment_time"]}')
                    print(reply["comment_text"])
                    print()
            print('---')
    print()