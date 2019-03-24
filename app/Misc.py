from os import system
from termcolor import cprint

class Sign:
    def logo(self):
        ps = lambda b: cprint(b, self)
        system('clear')
        print('\n')
        ps(" ██╗      ██████╗ ██╗  ██╗ █████╗ ███████╗██╗")
        ps(" ██║     ██╔═══██╗██║ ██╔╝██╔══██╗██╔════╝██║")
        ps(" ██║     ██║   ██║█████╔╝ ███████║███████╗██║")
        ps(" ██║     ██║   ██║██╔═██╗ ██╔══██║╚════██║██║")
        ps(" ███████╗╚██████╔╝██║  ██╗██║  ██║███████║██║")
        ps(" ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝")
        print('\n')
        return True
