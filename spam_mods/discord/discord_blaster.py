from ..agents.user_agents import agents
from ..proxies.grabProxies import freshProxies
from random import choice
import string
import threading
from requests import get, status_codes
from os import system
from time import sleep




class DiscordSpam:
    def __init__(self, discord_hook: str, mention_everyone: bool, add_random_junk: bool):
        p = freshProxies().randomProxy(True)
        self.proxy = {"http": p, "https": p}
        self.agent = {"User-Agent": choice(agents.split("\n"))}
        self.discord_hook = discord_hook
        self.everyone_mention = mention_everyone
        self.random_junk = add_random_junk
        self.thread_limit = 500

    def execute_spam(self):
        discord_spam = threading.Thread(target=self.execute_request,
                                        args=[self.discord_hook, self.agent, self.proxy, ])
        discord_spam.start()
        while threading.active_count() >= self.thread_limit:
            system("clear")
            discord_spam.join(0.75)
            print(f"\033[0;34mThread limit hit, waiting for threads to finish. "
                  f"{threading.active_count()}/{self.thread_limit}\033[0m")
            sleep(0.75)
            if threading.active_count() < self.thread_limit / 5:
                break


    @staticmethod
    def execute_request(target: str, set_agent: dict, set_proxy: dict):
        try:
            print("\033[0;36m")
            print(get(target, headers=set_agent, proxies=set_proxy).json())
            print("\033[0m")
        except Exception as e:
            print(f"\033[0;34m{e}\033[0m")


    @staticmethod
    def prep_data(random_junk: bool):
        match random_junk:
            case True:
                chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + \
                        string.printable
                data = '''
                {
                "id": "1007692564465459333",
                "type": 0,
                "content": "%s",
                "channel_id": "1007626923070988351",
                "author": {
                    "bot": true,
                    "id": "1007626960157028516",
                    "username": "get_rekt_skids",
                    "avatar": "",
                    "discriminator": "1337"
                },
                "attachments": [],
                "embeds": [],
                "mentions": [],
                "mention_roles": [],
                "pinned": false,
                "mention_everyone": true,
                "tts": true,
                "timestamp": "2022-08-12T16:50:29.391000+00:00",
                "edited_timestamp": null,
                "flags": 0,
                "components": [],
                "webhook_id": "1007626960157028516"
                }
                ''' % ''.join(choice(chars) for x in range(25, 500))
                return data
            case _:
                data = '''
                    {
                    "id": "1007692564465459333",
                    "type": 0,
                    "content": "%s",
                    "channel_id": "1007626923070988351",
                    "author": {
                        "bot": true,
                        "id": "1007626960157028516",
                        "username": "get_rekt_skids",
                        "avatar": "",
                        "discriminator": "1337"
                    },
                    "attachments": [],
                    "embeds": [],
                    "mentions": [],
                    "mention_roles": [],
                    "pinned": false,
                    "mention_everyone": true,
                    "tts": true,
                    "timestamp": "2022-08-12T16:50:29.391000+00:00",
                    "edited_timestamp": null,
                    "flags": 0,
                    "components": [],
                    "webhook_id": "1007626960157028516"
                    }
                    ''' % 'GET YOUR OWN SHIT SKIDS.'
                return data



