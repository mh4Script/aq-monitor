import os
import sys
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
from backend.models.airdata import AirData
from backend.models.userdata import UserData


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    import pdb;pdb.set_trace()
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        
        raw_airdata =[
            {
                'airdata_gps_location': '123,456',
                'airdata_co2': 1.222,
                'airdata_pm25': 1.232,
                'airdata_pm10': 1.234,
                'airdata_temperature': '12 c',
                'airdata_device': 'A'
            },
            {
                'airdata_gps_location': '133,456',
                'airdata_co2': 1.222,
                'airdata_pm25': 1.232,
                'airdata_pm10': 1.234,
                'airdata_temperature': '32 c',
                'airdata_device': 'B',
            },
            {
                'airdata_gps_location': '1223,1456',
                'airdata_co2': 1.222,
                'airdata_pm25': 1.232,
                'airdata_pm10': 1.234,
                'airdata_temperature': '32 c',
                'airdata_device': 'C'
            },
            {
                'airdata_gps_location': '122.3,145.6',
                'airdata_co2': 1.222,
                'airdata_pm25': 1.232,
                'airdata_pm10': 1.234,
                'airdata_temperature': '32 c',
                'airdata_device': 'D'
            },
        ]
        
        default_airdata = []
        for row in raw_airdata:
            default_airdata.append(AirData(
                airdata_gps_location = row['airdata_gps_location'],
                airdata_co2 = row['airdata_co2'],
                airdata_pm25 = row['airdata_pm25'],
                airdata_pm10 = row['airdata_pm10'],
                airdata_temperature = row['airdata_temperature'],
                airdata_device = row['airdata_device'],
        ))
        dbsession.add_all(default_airdata)
        
        default_userdata = UserData(
            userdata_name = 'jhon doe',
            userdata_email = 'jhon.doe@gmail.com',
            userdata_wa = '1234444',
        )
        dbsession.add(default_userdata)
