from importlib.metadata import version as _pkg_version, PackageNotFoundError

try:
    __version__ = _pkg_version('hungercore')
except PackageNotFoundError:
    __version__ = '0.0.0'

from .messagerouter import MessageRouter
from . import email, webhook, utils


__all__ = [
    '__version__',
    'MessageRouter',
    'email',
    'webhook',
    'utils',
]
