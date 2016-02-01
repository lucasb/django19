import logging

from django.shortcuts import render
from django.template import RequestContext


def not_authorazed(request):
    return render(request, 'error/status.html', {'code': 400, 'message': 'Not Authorized'}, status=400)

def page_not_found(request):
    logging.error('Item was not found.')
    return render(request, 'error/status.html', {'code': 404, 'message': 'Not Found'}, status=404)

def server_error(request):
    return render(request, 'error/status.html', {'code': 500, 'message': 'Internal Error'}, status=500)
