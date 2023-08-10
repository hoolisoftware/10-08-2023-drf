from pprint import pprint
from colorama import init as colorama_init
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style # noqa

from rest_framework.decorators import api_view
from rest_framework.response import Response


just_fix_windows_console()
colorama_init()


@api_view(['GET', 'POST'])
def request_parsing(request):
    '''
    Request
        .data
        .query_params
        .parsers
    '''
    print(Fore.GREEN)

    print('.data =')
    pprint(request.data)
    print()

    print('.query_params =')
    pprint(request.query_params)
    print()

    print('.parsers =')
    pprint(request.parsers)
    print()

    print(Style.RESET_ALL)

    return Response({'message': 'Request parsing point. Look to console'})


@api_view()
def content_negotiation(request):
    '''
    Request
        .user
        .auth
        .authenticators
    '''
    print(Fore.GREEN)

    print('.user =')
    pprint(request.user)
    print()

    print('.auth =')
    pprint(request.auth)
    print()

    print('.authenticators =')
    pprint(request.authenticators)
    print()

    print(Style.RESET_ALL)

    return Response({'message': 'Content negotiation point. Look to console'})
