import sys
import requests

# print(requests.__file__) # /home/gk/venv36/lib/python3.6/site-packages/requests/__init__.py
# /home/gk/venv36/lib/python3.6/site-packages/requests/exceptions.py

url = sys.argv[1]
print(url)
try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
except requests.Timeout:
    print("Timeout, url:", url)
except requests.HTTPError as err:
    code = err.response.status_code
    print("url error: {0}, return code: {1}".format(url, code))
except requests.RequestException:
    print("Downloading error url:", url)
else:
    print(response.content)
