import httpx


class CloseSystemSkill:
    def __init__(self):
        self.keyword = ["关电脑", "关闭电脑", "关机"]
        self.url = "http://127.0.0.1:19001"

    def handle(self, message):
        if message not in self.keyword:
            return
        res = self.request()
        if res.status_code == 200:
            return "已经关机"
        else:
            return "关机失败"

    def request(self):
        response = httpx.request("post", self.url)
        return response
