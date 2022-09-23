from .flex_uri_base import FlexUriBase
from dataclasses import dataclass
from python.flex_uri.parsed_uri import ParsedUri
from typing import Union
import requests


# This is just a passthrough for reading a HTTP endpoint
def scheme():
    return "http"

def factory_build(parsed_uri:ParsedUri):
    return HttpUri.wrap(uri=parsed_uri)


@dataclass
class HttpUri(FlexUriBase):
    uri:ParsedUri

    # this is kept as not a proprty to match the pathlib Path API
    def is_dir(self)->bool:
        return False
    # this is kept as not a proprty to match the pathlib Path API
    def is_file(self)->bool:
        assert False, "NOT IMPLEMENTED"
        #return Redis().hexists(self.hash_name, self.field_name)==1
    @property
    def has_path(self)->bool:
        return False

    @property
    def read_only(self)->bool:
        return True
    


    @staticmethod
    def wrap(uri=Union[ParsedUri, str])->"HttpUri":
        if isinstance(uri, str):
            uri=ParsedUri.parse(uri)
        assert isinstance(uri, ParsedUri)
        assert uri.scheme==scheme()
        # assert len(uri.parts)==3
        # assert uri.parts[0]=="/"
        assert False, "NOT IMPLEMENTED"        
        #return RedisHashUri(uri=uri)





    def read(self, *, offset:int=None, length:int=None)->bytes:
        return requests.get(str(self.uri)).read()

        # # ignore offset and length
        # r = Redis().hget(self.hash_name, self.field_name)  #, "aa", "bb", b"\xcc")
        # if offset is not None:
        #     if length is not None:
        #         return r[offset:length+offset]
        #     return r[offset:]
        # if length is not None:
        #     return r[:length]
        # return r
            

    # def write(self, *, value:bytes)->int:
    #     assert False, "NOT IMPLEMENTED"
    #     # Redis().hset(self.hash_name, self.field_name, value)
    #     # return len(value)


