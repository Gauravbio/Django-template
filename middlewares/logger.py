import time
import logging

logger = logging.getLogger('django')

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Start time
        start_time = time.time()

        response = self.get_response(request)

        time_elapsed = time.time() - start_time

        # Log the request type, time elapsed, and endpoint
        logger.info(
            f'RequestType={request.method}, Endpoint={request.path}, TimeElapsed={time_elapsed:.2f}s'
        )

        return response
