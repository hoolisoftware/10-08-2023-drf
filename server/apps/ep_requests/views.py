from rest_framework.decorators import api_view
from rest_framework.response import Response

from utils import print_attribute


@api_view(['GET', 'POST'])
def request_parsing(request):
    '''
    Request
        .data
        .query_params
        .parsers
    '''
    print_attribute('data', request.data)
    print_attribute('query_params', request.query_params)
    print_attribute('parsers', request.parsers)

    return Response({'message': 'Request parsing point. Look to console'})


@api_view()
def content_negotiation(request):
    '''
    Request
        .accepted_renderer
        .accepted_media_type
    '''
    print_attribute('accepted_renderer', request.accepted_renderer)
    print_attribute('accepted_media_type', request.accepted_media_type)

    return Response({'message': 'Content negotiation point. Look to console'})


@api_view()
def authentication(request):
    '''
    Request
        .user
        .auth
        .authenticators
    '''
    print_attribute('user', request.user)
    print_attribute('auth', request.auth)
    print_attribute('authenticators', request.authenticators)

    return Response({'message': 'Authentication point. Look to console'})


@api_view(['GET', 'POST'])
def browser_enhancements(request):
    '''
    Request
        .method
        .content_type
        .stream
    '''
    print_attribute('method', request.method)
    print_attribute('content_type', request.content_type)
    print_attribute('attribute', request.attribute)

    return Response({'message': 'Authentication point. Look to console'})
