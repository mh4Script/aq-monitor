from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='home', renderer='json')
def home(request):
    return {'project': 'air monitor backend v0'}
