import requests

class APIClient:

    def get(self, url, headers=None):
        return requests.get(url, headers=headers)

    def getsingleObjectByid(self,url,id,headers=None):
        return requests.get(f"{url}/{id}")

    def post(self, url, payload=None, headers=None):
        return requests.post(url, json=payload, headers=headers)

    def put(self, url, payload=None, headers=None):
        return requests.put(url, json=payload, headers=headers)

    def delete(self, url, headers=None):
        return requests.delete(url, headers=headers)
