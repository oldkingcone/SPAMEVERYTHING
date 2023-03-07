from requests import get
from random import choice
from os import getenv

class freshProxies:
    def __init__(self):
        self.proxy_types = [
                "socks4",
                "socks5",
                "https"
                ]
        self.proxy_list = set()

    def generateproxylist(self):
        for proxy in self.proxy_types:
            for i in get(f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol="
                         f"{proxy}&timeout=10000&country=all&ssl=all&anonymity=all").content:
                self.proxy_list.add(f"{proxy}://{str(i)}")

    def regenproxies(self):
        self.generateproxylist()

    def randomProxy(self, use_tor: bool):
        if not use_tor:
            try:
                t = choice(list(self.proxy_list))
            except IndexError:
                self.regenproxies()
                t = choice(list(self.proxy_list))
            self.proxy_list.remove(t)
            return t
        else:
            if getenv("TOR_PROXY") is not None:
                return str(getenv("TOR_PROXY"))
            else:
                return "socks5h://127.0.0.1:9050"
