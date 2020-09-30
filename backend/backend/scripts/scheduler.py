# create simple scheduler
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from backend.models.dummydatadevice import get_data_from_device, set_new_data

DEVICES = ['A', 'B', 'C', 'D']

def update_data_from_device(scheduler, settings):
    for device in DEVICES:
        new_data = get_data_from_device(device)
        jobid = 'updatedata_{}'.format(device)
        jobname = 'update data from device_{}'.format(device)
        scheduler.add_job(set_new_data,
            id=jobid,
            name=jobname,
            kwargs={'get_data_from_device': get_data_from_device, 'device': device, 'settings': settings},
            trigger='interval',
            seconds = 5,
        )

def add_scheduler(settings):
    scheduler = BackgroundScheduler()
    scheduler.start()
    update_data_from_device(scheduler, settings)
    atexit.register(lambda: scheduler.shutdown())