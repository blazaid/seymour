from rest_framework.response import Response
from rest_framework.views import APIView


class StatusView(APIView):
    """ Checks the status of the service. """

    def get(self, request, format=None):
        """ Returns the status of the service. """
        return Response({'status': 'ok'})
