import transaction
from pyramid.threadlocal import get_current_registry
from random import randint
from backend.models import (
    get_engine,
    get_session_factory,
    get_tm_session,
)
from backend.models.airdata import AirData
from backend.models.constanta import (
    CO2_HEALTH_THRESHOLD,
    PM25_HEALTH_THRESHOLD,
    PM10_HEALTH_THRESHOLD
)

def get_co2():
    return randint(0, 5)

def get_pm25():
    return randint(0, 5)

def get_pm10():
    return randint(0, 10)

def get_airdata_temperature():
    return randint(0, 10)

def get_data_from_device(device):
    print('get data from device {}'.format(device))
    return {
        'airdata_co2': get_co2(),
        'airdata_pm25': get_pm25(),
        'airdata_pm10': get_pm10(),
        'airdata_temperature': get_airdata_temperature(),
        'airdata_device': device,
    }
    
def set_new_data(get_data_from_device, device, settings):
    # update data in sqllite
    engine = get_engine(settings)
    session_factory = get_session_factory(engine)
    dbsession = get_tm_session(session_factory, transaction.manager)
    new_data = get_data_from_device(device)
    with transaction.manager:
        dbsession.query(AirData).filter(AirData.airdata_device == new_data['airdata_device']).update({
            AirData.airdata_co2: new_data['airdata_co2'],
            AirData.airdata_pm25: new_data['airdata_pm25'],
            AirData.airdata_pm10: new_data['airdata_pm10'],
            AirData.airdata_temperature: new_data['airdata_temperature'],
            AirData.airdata_device: new_data['airdata_device']
        })

def check_health_threshold():
    # check health treshold every 1 minute
    # this will mock function to measure the air health threshold
    pass