from pprint import pprint

from colorama import just_fix_windows_console as colorama_just_fix_windows_console
from colorama import init as colorama_init
from colorama import Fore, Back, Style # noqa


def print_attribute(attribute_name, value):
    colorama_just_fix_windows_console()
    colorama_init()
    print(Fore.GREEN)
    print(f'.{attribute_name} =')
    pprint(value)
    print(Style.RESET_ALL)
