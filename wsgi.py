import os

from devpi_server.config import parseoptions
from devpi_server.main import XOM


myargs = ['',]

if 'GONDOR_DATA_DIR' in os.environ:
  datadir = os.path.join(os.environ['GONDOR_DATA_DIR'], '.devpi', 'server')
  secretfile = os.path.join(datadir, 'secretfile')
  
  myargs.append('--datadir=%s' % datadir)
  myargs.append('--secretfile=%s' % secretfile)


def make_application(args):
    """ entry point for making an application object with defaults. """
    config = parseoptions(args)
    return XOM(config).create_app()

application = make_application(myargs)