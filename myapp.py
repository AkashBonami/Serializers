import requests
import json
URL="http://127.0.0.1:8000/studentcreate/"

data={
    'name':'Prakhar',
    'roll':420,
    'city':'Uttrakhand',
}

json_data= json.dumps(data)
print("===============")
r=requests.post(url=URL , data=json_data)
print("===============")

# data = r.json()
print(r.json)
