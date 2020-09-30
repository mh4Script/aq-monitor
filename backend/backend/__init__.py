from pyramid.config import Configurator
from backend.scripts.scheduler import add_scheduler


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('.models')
    config.include('.routes')
    config.scan()
    add_scheduler(settings)
    return config.make_wsgi_app()
