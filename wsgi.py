from sys import argv
from os import environ, path

datadir = path.join(environ['GONDOR_DATA_DIR'], '.devpi', 'server')
secretfile = path.join(datadir, 'secretfile')

argv.append('--datadir=%s' % datadir)
argv.append('--secretfile=%s' % secretfile)

from devpi_server.main import main

application = main()