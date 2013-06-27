from sys import argv
from os import environ, path

from devpi_server.main import make_application


datadir = path.join(environ['GONDOR_DATA_DIR'], '.devpi', 'server')
secretfile = path.join(datadir, 'secretfile')

argv.append('--datadir=%s' % datadir)
argv.append('--secretfile=%s' % secretfile)

application = make_application()
