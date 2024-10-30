from facebook_scraper import get_posts

group_id = '1740036226559286'
MAX_COMMENT = 10
try:
    for post in get_posts(group=group_id, base_url="https://mbasic.facebook.com/",start_url="https://mbasic.facebook.com/groups/1740036226559286", cookies='cookies.txt', options={"comments": MAX_COMMENT, "progress": True}):
        print(post)
        try:
            
            comments = post['comments_full']
            print(comments)
            # process comments as you want...
            for comment in comments:

                # e.g. ...print them
                print(comment)

                # e.g. ...get the replies for them
                for reply in comment['replies']:
                    print(' ', reply)


            print(post['text'][:50])
        except KeyError:
            print("error")
except Exception as e:
    print(f"error: {e}")

