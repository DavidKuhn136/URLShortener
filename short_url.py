import requests

# account credentials - bitly
username = "sssssssss" #change
password = "ppppppppp" #change

# get the access token
auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))
if auth_res.status_code == 200:
    # response ok?, get access code
    access_token = auth_res.content.decode()
    print("[!] Got access token:", access_token)
else:
    print("[!] Cannot get acces token, exiting...")
    exit()

# construct the requet headers
headers = {"Authorization": f"Bearer {access_token}"}

# get the group UID
groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
if groups_res.status_code == 200:
    #response ok? get GUID
    groups_data = groups_res.json()['groups'][0]
    guid = groups_data['guid']
else:
    print("[!] Cannot get GUID, exiting...")
    exit()

# the URL to shorten
url = "https://www.google.com"
# make the POST request to get shortened URL for 'url'
shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
if shorten_res.status_code == 200:
    #response ok?, get short url
    link = shorten_res.json().get("link")
    print("Shortened URL:", link)