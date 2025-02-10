import http.client

conn = http.client.HTTPSConnection("sephora.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "aa958f4fcbmsh4cc2603e95193adp135146jsn080abdce0fda",
    'x-rapidapi-host': "sephora.p.rapidapi.com"
}

conn.request("GET", "/categories/list?categoryId=cat150006", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))