from colorama import Fore

LOGO = """

 _       __               ______            __    
| |     / /___ __   _____/_  __/___  ____  / /____
| | /| / / __ `/ | / / _ \/ / / __ \/ __ \/ / ___/
| |/ |/ / /_/ /| |/ /  __/ / / /_/ / /_/ / (__  ) 
|__/|__/\__,_/ |___/\___/_/  \____/\____/_/____/  
                                                  
  
"""
MENU = f"""
                                   {Fore.CYAN}[{Fore.WHITE}01{Fore.CYAN}] FiveGet Lookup FiveM   {Fore.CYAN}[{Fore.WHITE}06{Fore.CYAN}] Ip LookUp
                                   {Fore.CYAN}[{Fore.WHITE}02{Fore.CYAN}] RedTiger               {Fore.CYAN}[{Fore.WHITE}07{Fore.CYAN}] Cheap Market
                                   {Fore.CYAN}[{Fore.WHITE}03{Fore.CYAN}] Tabaco V2              {Fore.CYAN}[{Fore.WHITE}08{Fore.CYAN}] GTA 5
                                   {Fore.CYAN}[{Fore.WHITE}04{Fore.CYAN}] Nexus Tool             {Fore.CYAN}[{Fore.WHITE}09{Fore.CYAN}] Free Movies
                                   {Fore.CYAN}[{Fore.WHITE}05{Fore.CYAN}] Fivem IP               {Fore.CYAN}[{Fore.WHITE}10{Fore.CYAN}] Twitch Followers
"""

def MainMenu():
    print(Fore.CYAN + LOGO)
    print(MENU)
