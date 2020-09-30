from pyramid.view import view_config
from backend.models.airdata import AirData


@view_config(route_name='air-quality-data')
class AirQualityDataView(object):
    def __init__(self, request):
        self.request = request

    def get(self):
        data = self.request.dbsession.query(AirData).all()
        result = []
        for row in data:
            result.append({
                'airdata_gps_location': row.airdata_gps_location,
                'airdata_co2': row.airdata_co2,
                'airdata_pm25': row.airdata_pm25,
                'airdata_pm10': row.airdata_pm10,
                'airdata_temperature': row.airdata_temperature
            })
        return {'result': result}