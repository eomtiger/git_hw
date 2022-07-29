import requests

#방법 1
# res = requests.get('https://api.agify.io?name=heewon')
# data = res.json()
# print(data, type(data))
# print(data.get('name'))

URL = 'https://api.agify.io/'
params = {
    'name' : 'heewon'
}
res = requests.get(URL,params = params)
data = res.json()
print(data)
print(data.get('heewon'))