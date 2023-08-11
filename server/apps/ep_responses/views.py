from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from django.template import Context

from utils import print_attribute


@api_view()
def creating_responses(request):
    response = Response(
        data={},
        status=None,
        template_name=None,
        headers=None,
        content_type=None
    )
    return response


@api_view()
def attributes(request):
    '''
        Response
            .data
            .status_code
            .content
            .template_name
            .accepted_renderer
            .accepted_media_type
            .renderer_context
    '''

    response = Response({})

    print_attribute('data', response.data)
    print_attribute('status_code', response.status_code)
    # print_attribute('content', response.content)
    print_attribute('template_name', response.template_name)
    # print_attribute('accepted_renderer', response.accepted_renderer)
    # print_attribute('accepted_media_type', response.accepted_media_type)
    # print_attribute('renderer_context', response.renderer_context)

    return response
