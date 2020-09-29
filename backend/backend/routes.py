from backend.views.airqualitydata import AirQualityDataView
from backend.views.userdata import UserDataView

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    
    # route air quality data
    config.add_route('air-quality-data', '/air-quality-data')
    config.add_view(
        AirQualityDataView, route_name='air-quality-data', attr='get', request_method='GET', renderer='json')
    config.add_view(
        AirQualityDataView, route_name='air-quality-data', attr='update', request_method='POST', renderer='json')
    
    # route user data
    config.add_route('user-data', '/user-data')
    config.add_view(
        UserDataView, route_name='user-data', attr='get', request_method='GET', renderer='json')
    config.add_view(
        UserDataView, route_name='user-data', attr='update', request_method='POST', renderer='json')
