import requests


class Http:
    # curl get
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
        # if r.status_code == 200:
        #     if return_json is True:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''

    # post
    def post(self, url, params, return_jsop=True):
        r = requests.post(url, params)
        if return_jsop is True:
            return r.json()
        else:
            return r
        pass
