import http.client

conn = http.client.HTTPSConnection("apidojo-hm-hennes-mauritz-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "aa958f4fcbmsh4cc2603e95193adp135146jsn080abdce0fda",
    'x-rapidapi-host': "apidojo-hm-hennes-mauritz-v1.p.rapidapi.com"
}

conn.request("GET", "/products/list?country=us&lang=en&currentpage=0&pagesize=30&categories=men_all&concepts=H%26M%20MAN", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))