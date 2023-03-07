from requests import get
from faker import Faker
from os import urandom, system
from random import randint, choice
from psutil import cpu_percent
import threading
from ..agents import user_agents


class spamGrabify:
    def __init__(self):
        self.thread_limit = 100
        self.cpu_percent = 80
        Faker.seed(urandom(randint(1024, 2048)))
        self.fake_fucks = Faker()
        self.agents_list = str(user_agents).split("\n")

    def getRandomAgents(self):
        return choice(self.agents_list)

    def executeRequest(self, grabify_url: str, proxy: str):
        try:
            fuck_skids = get(grabify_url,
                   headers = {
                           "User-Agent": self.getRandomAgents(),
                           "Connection": "close",
                           "Charset": "utf-8",
                           "Accept": "*/*",
                           "Referrer": "https://redirecthost.online/"
                           },
                   proxies = {
                           "http": f"{proxy}",
                           "https": f"{proxy}"
                           }
                             )
            if fuck_skids.status_code:
                print(f"\033[0;33mSuccessful!\n->Status Code: {fuck_skids.status_code}\n{fuck_skids.text}\033[0m")
            else:
                print(f"\033[0;33mUnable to reach with: {proxy}\033[0m")
        except Exception as e:
            print(f"\033[0;31mError occured: {str(e)}\033[0m")
            print(f"\033[0;31mUsing: {str(proxy)}\033[0m")

    def buildThreads(self, grabify, proxy: str):
        grabifyspam = threading.Thread(target = self.executeRequest, args=[grabify, proxy, ])
        grabifyspam.start()
        while threading.active_count() >= self.thread_limit or int(str(cpu_percent()).split(".")[0]) >= \
                self.cpu_percent:
            system("clear")
            print(f"\033[0;31mCpu or thread limit hit: \nCPU Load: {cpu_percent()}\nThreads: {threading.active_count()}"
                  f"/{self.thread_limit}\033[0m")
            grabifyspam.join(0.75)
