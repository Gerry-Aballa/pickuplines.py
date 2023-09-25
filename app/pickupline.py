import requests


api_url = "http://ec2-3-7-73-121.ap-south-1.compute.amazonaws.com:8000/lines/random"

pickupline_str = ""
def get_pickupline():
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            global pickupline_str
            pickupline_str = f"{data['mood']} mood. \n{data['pickupline']}"

            print(pickupline_str)

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ValueError as e:
        print(f"JSON parsing error: {e}")
