from pyramid.view import view_config

@view_config(route_name='user-data')
class UserDataView(object):
    def __init__(self, request):
        self.request = request

    def get(self):
        return {'result': 'get data'}

    def update(self):
        return {'result': 'data updated'}