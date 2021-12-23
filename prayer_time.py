import requests
from pprint import pprint as print


url = "https://dailyprayer.abdulrcs.repl.co/api/busan"
response = requests.get(url)
data = response.json()
print(data['city'])
print(data['date'])


# Hanafi
for prayer in data["today"]:
    if prayer == "Asr":
        print(f"{prayer}: {int(data['today'][prayer].split(':')[0]) + 1}:{int(data['today'][prayer].split(':')[1]) - 20}")
    else:

        print(prayer + ": " + data["today"][prayer])
# url = "https://www.muslimpro.com/Prayer-times-Busan-South-Korea-1838524?date=&convention=MWL&asrjuristic=Hanafi"
#
# url2 = "http://www.muslimpro.com/muslimprowidget.js?cityid=1838524"
#
# res = requests.get(url2)
#
# print(res.text)




