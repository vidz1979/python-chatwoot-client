import httpx


class HttpClient:
    def __init__(self, api_url, api_token):
        self.api_token = api_token
        self.api_url = api_url
        self.headers = {
            "api_access_token": f"{api_token}",
            "Content-Type": "application/json",
        }

    def _request(self, method, url, query=None, data=None):
        with httpx.Client() as client:
            response = client.request(
                method,
                f"{self.api_url}{url}",
                headers=self.headers,
                params=query,
                json=data,
            )
            response.raise_for_status()
            return response.json()

    def get(self, url, query=None):
        return self._request("GET", url, query)

    def post(self, url, data=None):
        return self._request("POST", url, data=data)

    def put(self, url, data=None):
        return self._request("PUT", url, data=data)

    def delete(self, url):
        return self._request("DELETE", url)

    def patch(self, url, data=None):
        return self._request("PATCH", url, data=data)
