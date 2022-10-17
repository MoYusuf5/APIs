# APIs with Python
# install requests
# pip install requests

import requests
# Get
request_bbc_status_code = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")
# check the outcome of our API call
# print(request_bbc_status_code.status_code)
# let's check the header
# print(request_bbc_status_code.headers)
# let's check the content available
# print(request_bbc_status_code.content)

# print the status code with success message
print(f"{request_bbc_status_code.status_code} : request is successful")
# print unsuccesful if status code is not 200
request_incorrect_url_status_code = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnew")
print(f"{request_incorrect_url_status_code.status_code} : request is unsuccessful")