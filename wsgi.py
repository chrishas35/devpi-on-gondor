from sys import argv
from os import environ, path

from devpi_server.config import parseoptions
from devpi_server.main import XOM


datadir = path.join(environ['GONDOR_DATA_DIR'], '.devpi', 'server')
secretfile = path.join(datadir, 'secretfile')

argv.append('--datadir=%s' % datadir)
argv.append('--secretfile=%s' % secretfile)

config = parseoptions(sys.argv)

application = XOM(config).create_app()
