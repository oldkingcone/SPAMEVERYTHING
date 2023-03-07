from time import sleep
from requests import get
from urllib.parse import urlencode, quote_plus
from faker import Faker
from faker.providers import internet
from os import urandom, system
from string import ascii_letters, digits
from random import randint, choice
from json import dumps
from psutil import cpu_percent
import threading

class SpamTelegram:
    def __init__(self):
        self.threadLimit = 100
        self.cpuLimit = 80
        Faker.seed(urandom(randint(256, 4096)))
        self.fake_shit = Faker()
        self.fake_shit.add_provider(internet)
        self.proxy = "socks5h://127.0.0.1:9050"

    def buildData(self):
        charset = ascii_letters + digits
        name = self.fake_shit.name()
        fake_pw = ''.join(choice(charset) for i in range(randint(5, 15)))
        fake_2fac = ''.join(choice(charset) for i in range(6))
        return f"IP:+{self.fake_shit.ipv4_private()}+Page+name:+https://facebook.com/{name}+Email/Mobile:+" \
               f"{self.fake_shit.ascii_email()}+Full+name:+{name}+Additional+info:++Password:{fake_pw}" \
               f"+2Fac:+{fake_2fac}" + "reply_markup={\"inline_keyboard\":[[{\"text\":\"2FAAGAIN\"," \
                                       "\"url\":\"https://alloalloteam.team/1666201256135_b35311fb-43bf-438b-a645" \
                                       "-7eb8d47910d8/2FAAGAIN\"},{\"text\":\"PASSWD\"," \
                                       "\"url\":\"https://alloalloteam.team/1666201256135_b35311fb-43bf-438b-a645" \
                                       "-7eb8d47910d8/PASSWDAGAIN\"},{\"text\":\"REQUIREEMAIL\"," \
                                       "\"url\":\"https://alloalloteam.team/1666201256135_b35311fb-43bf-438b-a645" \
                                       "-7eb8d47910d8/REQUIREEMAIL\"},{\"text\":\"FINISH\"," \
                                       "\"url\":\"https://alloalloteam.team/1666201256135_b35311fb-43bf-438b-a645" \
                                       "-7eb8d47910d8/FINISH\"}]]}"

    def buildRequest(self, telegram_url: str):
        try:
            spam_blast = get(
                f"{telegram_url}&text=TURD+EMAIL%0D%0A{self.buildData()}",
                proxies = {
                        "http": f"{self.proxy}", "https": f"{self.proxy}"
                        },
                headers = {
                        "Accept": "application/json"
                        }
                )
            if spam_blast.status_code:
                pretty_format = dumps(spam_blast.json(), indent = 4)
                print(f"\033[0;32m{pretty_format}\033[0m")
            else:
                print(f"\033[0;31m{spam_blast.status_code}\n{spam_blast.content}\033[0m")
        except Exception as e:
            print(f"\033[0;31m{e}\033[0m")

    def startThreads(self, telegram_url: str):
        holyshitbatman = threading.Thread(target = self.buildRequest, args = [telegram_url, self.proxy, ])
        holyshitbatman.start()
        while threading.active_count() >= self.threadLimit or int(
                str(cpu_percent()).split(".")[0]
                ) >= self.cpuLimit:
            system("clear")
            current = threading.active_count()
            print(f"Waiting for threads to go away........{current}/{self.threadLimit}")
            holyshitbatman.join(0.75)
            sleep(1)