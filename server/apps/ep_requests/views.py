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
        .accepted_renderer
        .accepted_media_type
    '''
    print(Fore.GREEN)

    print('.accepted_renderer =')
    pprint(request.accepted_renderer)
    print()

    print('.accepted_media_type =')
    pprint(request.accepted_media_type)
    print()

    print(Style.RESET_ALL)

    return Response({'message': 'Content negotiation point. Look to console'})


@api_view()
def authentication(request):
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

    return Response({'message': 'Authentication point. Look to console'})


@api_view(['GET', 'POST'])
def browser_enhancements(request):
    '''
    Request
        .method
        .content_type
        .stream
    '''
    print(Fore.GREEN)

    print('.method =')
    pprint(request.method)
    print()

    print('.content_type =')
    pprint(request.content_type)
    print()

    print('.stream =')
    pprint(request.stream)
    print()

    print(Style.RESET_ALL)

    return Response({'message': 'Authentication point. Look to console'})
