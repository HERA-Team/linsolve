try:
    from importlib.metadata import PackageNotFoundError
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import PackageNotFoundError
    from importlib_metadata import version

try:
    from ._version import version as __version__
except ModuleNotFoundError:  # pragma: no cover
    try:
        __version__ = version(__name__)
    except PackageNotFoundError:  # pragma: no cover
        # package is not installed
        __version__ = "unknown"

from .linsolve import *  # noqa
