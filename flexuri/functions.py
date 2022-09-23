from urllib.parse import urlparse
from pathlib import Path
from types import ModuleType
from flexuri.flex_uri_base import FlexUriBase


from .parsed_uri import ParsedUri
from flexuri import util_file_uri as file_uri
# from . import util_kv_cache as kvcache_uri
# from . import util_redis_hash as redis_hash_uri


# LIBS=[redis_hash_uri,file_uri,kvcache_uri]
LIBS=[file_uri]
INSTALLED_LIBS=[]
def _libs():
    r =  [file_uri]
    r.extend(INSTALLED_LIBS)
    return r


# factory function
def wrap(uri:str)->FlexUriBase:
    parsed_uri =  ParsedUri.parse(uri_str=uri)
    for lib in _libs():
        if parsed_uri.scheme == lib.scheme():
            return lib.factory_build(parsed_uri)
    assert False


def build_from_file_path(path:Path):
    return wrap(uri= f"{file_uri.scheme()}://{path.absolute()}")

def install(obj:FlexUriBase):
    assert isinstance(obj, ModuleType), "object must be a python module"
    for attr_name in ["scheme", "path", "suffix", "stem", "as_json", "get_blob"]:
        assert hasattr(obj, attr_name)
    INSTALLED_LIBS.append(obj)
    assert False

