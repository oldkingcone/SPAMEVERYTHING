from ..proxies.grabProxies import freshProxies
from ..agents.user_agents import agents
from requests import get, status_codes
from random import choice


class TestConnection:
    def __init__(self, url: str):
        self.proxy = freshProxies().randomProxy(True)
        self.agent = choice(agents.split("\n"))
        if not url.startswith("http"):
            url = f"http://{url}"
        self.target = url

    def begin_test(self):
        return self.attempt_connection(self.target, {"http": self.proxy, "https": self.proxy}, {"User-Agent": self.agent})

    @staticmethod
    def attempt_connection(target: str, proxies: dict, headers: dict) -> dict:
        try:
            test_connection = get(target, proxies=proxies, headers=headers)
            if test_connection.status_code is not None:
                return {
                    "Success": True,
                    "Schema": "http://",
                    "StatusCode": test_connection.status_code,
                    "Error": None
                }
            else:
                return {
                    "Success": False,
                    "Schema": "http://",
                    "StatusCode": test_connection.status_code,
                    "Error": None
                    }
        except (ConnectionError, Exception) as e:
            return {
                "Success": False,
                "Schema": None,
                "StatusCode": None,
                "Error": str(e)
            }