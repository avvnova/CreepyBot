import datetime
import platform
import socket
import sys

from .cogs import *
from .core.config import *
#from .events import *
#from .messages import *
#from .setup import *


def version():
    return "v0.0.1.0"


def config_version():
    return "0.1"  # do not edit this!


def time():
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")


def year():
    return str(datetime.datetime.now().year)


def platform():
    return platform.system() + " " + platform.release()


def hostname():
    return socket.gethostname()


def ip():
    return socket.gethostbyname(hostname())


def path():
    return sys.path