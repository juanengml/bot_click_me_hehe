from urllib2 import urlopen, Request
headers = {'Authorization': 'Token token=eebf8075f1d24f268bb2f15a4f159a95'}
url = "http://www.cepaberto.com/api/v2/ceps.json?cep=40010000"
json = urlopen(Request(url, None, headers=headers)).read()
print json


from urllib2 import urlopen, Request
headers = {'Authorization': 'Token token=eebf8075f1d24f268bb2f15a4f159a95'}
url = "http://www.cepaberto.com/api/v2/cities.json?estado=SP"
json = urlopen(Request(url, None, headers=headers)).read()
print json
                    
