from app.pickupline import get_pickupline
from app.twitter import sendTweet
from app.facebook import sendPost
import schedule
import time


def sendPosts():
    get_pickupline()
    sendTweet()
    sendPost()
    
sendPosts()
# schedule.ever().day.at("09:00").do(sendPosts)


# while True:
#     schedule.run_pending()

#     time.sleep(1)