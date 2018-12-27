from scrapepy.scrapepy import ScrapePy
import os, sys, random

hashtag = input()
username = input()

s = ScrapePy()

# Download pictures by username
s.scrape_by_username(username)
# Download pictures by hashtag
s.scrape_by_hashtag(hashtag)


# Download videos by username
s.scrape_videos_by_username(username)

# Download videos by hashtag
s.scrape_videos_by_hashtag(hashtag)

pause = input("Press any key to exit...")
