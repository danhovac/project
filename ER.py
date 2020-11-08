import requests
import xml.etree.ElementTree as ET
url = "http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEmrrmRltmUsefulSckbdInfoInqire?serviceKey=0fjXTO4xbqzM%2BHX7FNzr8tMXWr1n7L%2Fk3O0VzZoza0lLFs8SDlUkYt%2Bt%2FgAneK3dfZc5ZIyGXNenUzASXKfhWA%3D%3D&STAGE1=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&STAGE2=%EA%B0%95%EB%82%A8%EA%B5%AC&pageNo=1&numOfRows=10"
r = requests.get(url=url)
print(r.text)

root = ET.fromstring(r.text)
data = []
for item in root.find('body').find('items'):
    dict_data = {
        'nicu': item.find('hvncc').text,
        'ventilator':item.find('hv10').text,
        'hospital_name': item.find('dutyName').text,
        'nicu_call':item.find('hv12')
    }
    data.append(dict_data)
print(data)