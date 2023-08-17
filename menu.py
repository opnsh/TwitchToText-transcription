from colorama import init, Fore, Style

def visual():
    return r""" ______       _ __      __ ______   ______        __ 
/_  __/    __(_) /_____/ //_  __/__/_  __/____ __/ /_
 / / | |/|/ / / __/ __/ _ \/ / / _ \/ / / -_) \ / __/
/_/  |__,__/_/\__/\__/_//_/_/  \___/_/  \__/_\_\\__/ 
                                    opensh on Github
                                                     """

def cli():
    init(autoreset=True) 
    print(Fore.MAGENTA + visual())
    print(Fore.YELLOW + "Press ctrl+c to stop" + "\nResult in transcript.txt")
    print(Style.RESET_ALL)  

