import requests

commodityPrefix = "https://www.amazon.com/dp/"
commentPrefix = "https://www.amazon.com"
useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"


class amazonRequest:

    def __init__(self):
        self.commodityPrefix = commodityPrefix
        self.commentPrefix = commentPrefix
        self.useragent = useragent

    def request(self, request_uri):
        user_agent = {'User-agent': useragent}
        response = requests.get(request_uri, headers=user_agent)
        if (response.status_code == 404):
            print('Amazon Request Failed' + request_uri)
            return ""
        return response.text
