#!/usr/bin/env python3
from spam_mods.telegram import telegram_spammer
from spam_mods.grabify import grabifyspam
from spam_mods.proxies.grabProxies import freshProxies
from spam_mods.generic_spam.generic import GenericSpam
from spam_mods.verify_connection.testaroo import TestConnection
from spam_mods.discord.discord_blaster import DiscordSpam
from sys import argv


help = f'''
{argv[0]} (telegram|grabify|generic) url

If discord is supplied, you will need 2 additional arguments, one to mention everyone, and one to add junk data.
'''

try:
    if len(argv) < 2:
        print("forgot args.")
        print(f"\033[0;32m{help}\033[0m")
        exit(1)
    else:
        subset = freshProxies()
        subset.generateproxylist()
        check = TestConnection(argv[2]).begin_test()
        if check['Success']:
            match argv[1]:
                case "discord":
                    startthespam = DiscordSpam(argv[2], bool(argv[3]), bool(argv[4]))
                    while True:
                        startthespam.execute_spam()
                case "telegram":
                    startthespam = telegram_spammer.SpamTelegram()
                    while True:
                        startthespam.startThreads(argv[2])
                case "generic":
                    startthespam = GenericSpam()
                    while True:
                        startthespam.buildThreads(argv[2])
                case "grabify":
                    startthespam = grabifyspam.spamGrabify()
                    while True:
                        startthespam.buildThreads(argv[2], subset.randomProxy(use_tor = True))
                case _:
                    print(help)
        else:
            print("\033[0;31mIt appears as though the endpoint is not reachable. Please check and try again.\033[0m")
except KeyError:
    print("forgot args.")
    print(f"\033[0;32m{help}\033[0m")
    exit(1)