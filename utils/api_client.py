import requests

class APIClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)

    def get(self, endpoint, **kwargs):
        return self.session.get(self.base_url + endpoint, **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        return self.session.post(self.base_url + endpoint, data=data, json=json, **kwargs)

    def put(self, endpoint, data=None, json=None, **kwargs):
        return self.session.put(self.base_url + endpoint, data=data, json=json, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.session.delete(self.base_url + endpoint, **kwargs)