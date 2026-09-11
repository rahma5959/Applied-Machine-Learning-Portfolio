import requests

url = "http://127.0.0.1:5000/predict_web"
files = {"image": open("data/raw/image1.png","rb")}

r = requests.post(url, files=files)

assert r.status_code == 200
print("Test OK: /predict_web fonctionne correctement")