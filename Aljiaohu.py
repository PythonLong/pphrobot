import requests
class Tuling(object):
    def __init__(self):
        self.url = 'http://www.tuling123.com/openapi/api'
        self.json = {'key':'5d76973c7ae04267a85ff2daad9f3e64','info': None,'userid':1}

    def API(self,talk):
        self.json['info'] = talk
        r = requests.post(self.url,data=self.json)

        rdict = r.json()

        return rdict
tuling = Tuling()
if __name__ == "__main__":
    pass

