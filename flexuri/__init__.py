import sys

if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata

from flexuri.flex_uri_base import FlexUriBase
from flexuri.functions import wrap, install
# from cfs.cfs_builder import CFS_Builder
# from cfs.cfs_bytestream import CFS_Bytestream
# from cfs.cfs_file import CFS_File
# from cfs.exceptions import CFS_Error

try:
    __version__ = metadata.version("flexuri")
except metadata.PackageNotFoundError:
    __version__ = "99.99.99"



def int_or_str(value):
    try:
        return int(value)
    except ValueError:
        return value


VERSION = tuple(map(int_or_str, __version__.split(".")))


__all__ = [
    "FlexUriBase",
    "wrap", 
    "install",

]