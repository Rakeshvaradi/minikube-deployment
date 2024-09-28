import requests
URL="http://www.nonexistentwebsite12345.com"
def app_health(url):
    try:
        response=requests.get(url,timeout=5)
        if response.status_code == 200:
            return"UP"
        else:
            return "DOWN"
    except requests.RequestException:
        return "DOWN"

result=app_health(URL)
print(result)