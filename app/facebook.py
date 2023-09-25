import requests
from pickupline import pickupline_str
import os

page_id = os.environ.get("FB_PAGE_ID")
page_access_token = os.environ.get("FB_PAGE_ACCESS_TOKEN")

post_url = f'https://graph.facebook.com/v18.0/{page_id}/feed'

post_data = {
    'message': pickupline_str,
    'access_token': page_access_token
}

def sendPost():

    response = requests.post(post_url, data=post_data)

    print("FB posted successfully!")