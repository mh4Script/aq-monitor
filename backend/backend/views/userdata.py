from pyramid.view import view_config
from backend.models.userdata import UserData

@view_config(route_name='user-data')
class UserDataView(object):
    def __init__(self, request):
        self.request = request

    def get(self):
        query = self.request.dbsession.query(UserData)
        user = query.first()
        return {
            'result': {
                'username': user.userdata_name,
                'wa': user.userdata_wa,
                'email': user.userdata_email,
            }
        }

    # params id, wa, email
    def update(self):
        # TODO
        return {'result': 'data updated successfully'}