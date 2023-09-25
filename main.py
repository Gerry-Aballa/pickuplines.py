from app import pickupline, twitter, facebook
import schedule
import time


def sendPosts():
    pickupline.get_pickupline
    twitter.sendTweet
    facebook.sendPost
    

schedule.ever().day.at("09:00").do(sendPosts)


while True:
    schedule.run_pending()

    time.sleep(1)