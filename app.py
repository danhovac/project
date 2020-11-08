import requests
service_key = "0fjXTO4xbqzM%2BHX7FNzr8tMXWr1n7L%2Fk3O0VzZoza0lLFs8SDlUkYt%2Bt%2FgAneK3dfZc5ZIyGXNenUzASXKfhWA%3D%3D"
host = "http://apis.data.go.kr"
request_url = f"http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEmrrmRltmUsefulSckbdInfoInqire?serviceKey={service_key}&STAGE1=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&STAGE2=%EA%B0%95%EB%82%A8%EA%B5%AC&pageNo=1&numOfRows=10"
r = requests.get(url="http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEmrrmRltmUsefulSckbdInfoInqire?serviceKey=0fjXTO4xbqzM%2BHX7FNzr8tMXWr1n7L%2Fk3O0VzZoza0lLFs8SDlUkYt%2Bt%2FgAneK3dfZc5ZIyGXNenUzASXKfhWA%3D%3D&STAGE1=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&STAGE2=%EA%B0%95%EB%82%A8%EA%B5%AC&pageNo=1&numOfRows=10")
print(r.text)