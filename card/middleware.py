import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger('cards')


class RequestLogMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        logger.info(f'Request: {request.method} {request.get_full_path()}')

    @staticmethod
    def process_response(request, response):
        logger.info(f'Response: {response.status_code} {response.content}')
        return response
