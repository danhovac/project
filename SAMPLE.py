import urllib
import xml.etree.ElementTree as ET
import requests

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

base_url = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEmrrmRltmUsefulSckbdInfoInqire'
# qs = urllib.parse.urlencode(param)
# r = requests.get(url=f"{base_url}?{qs}")
# print(r.text)
# root = ET.fromstring(r.text)
# data = []
# for item in root.find('body').find('items'):
#     dict_data = {
#         'hvec': item.find('hvec').text,
#         'hospital_name': item.find('dutyName').text
#     }
#     data.append(dict_data)
# print(data)

# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('data.html')


@app.route('/emptybed', methods=['GET'])
def empty_beds():
    print(f'from client: {request.args.get("regiona")}')
    region = request.args.get("regiona")
    param = {
        'serviceKey': '0fjXTO4xbqzM+HX7FNzr8tMXWr1n7L/k3O0VzZoza0lLFs8SDlUkYt+t/gAneK3dfZc5ZIyGXNenUzASXKfhWA==',
        'STAGE1': '서울특별시',
        'STAGE2': region,
        'numOfRows': 500,
    }
    qs = urllib.parse.urlencode(param)
    r = requests.get(url=f"{base_url}?{qs}")
    # print(r.text)
    root = ET.fromstring(r.text)
    data = []
    for item in root.find('body').find('items'):
        # dict_data = {
        #     'hvec': item.find('hvec').text,
        #     'hospital_name': item.find('dutyName').text
        # }
        data.append(item.find('dutyName').text)
    # print(data)
    return jsonify({'result': 'success', 'beds_list': data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)