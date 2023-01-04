import requests 

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

rows = rjson['RealtimeCityAir']['row']

for a in rows:
    gu_name = a['MSRSTE_NM']
    gu_mise = a['IDEX_MVL']

    print(gu_name,gu_mise)