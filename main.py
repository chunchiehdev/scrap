from facebook_scraper import get_posts

group_id = '1740036226559286'
POST_ID= "https://mbasic.facebook.com/groups/1740036226559286/posts/1740037736559135"
MAX_COMMENT = 10
try:
    for post in get_posts(post_urls=[POST_ID], options={"comments": True,"reactors": True,"reactions":True,"allow_extra_requests": True, "progress": True,"extra_info":True}):
        print(post)
except Exception as e:
    print(f"error: {e}")

