from .flex_uri_base import FlexUriBase
from .parsed_uri import ParsedUri
from dataclasses import dataclass
from pathlib import Path

#from urllib.parse import urlparse, ParseResult


def scheme():
    return "file"
def factory_build(parsed_uri:ParsedUri):
    return FileUri(uri=parsed_uri)
@dataclass
class FileUri(FlexUriBase):
    uri:ParsedUri

    # this is kept as not a proprty to match the pathlib Path API
    def is_dir(self)->bool:
        return self.as_local_path.is_dir()

    # this is kept as not a proprty to match the pathlib Path API
    def is_file(self)->bool:
        return self.as_local_path.is_file()
    @property
    def has_path(self)->bool:
        return False
    

    @staticmethod
    def parse(uri_str:str)->"FileUri":
        parsed=ParsedUri.parse(uri_str)
        assert parsed.scheme==scheme()
        assert len(parsed.parts)==3
        assert parsed.parts[0]=="/"
        return FileUri(uri=parsed)


    @property
    def as_local_path(self)->Path:
        local_path=Path(self.path)
        assert local_path.exists()
        return local_path

    @property
    def as_file(self)->Path:
        assert self.as_local_path.is_file()
        return self.as_local_path

    @property
    def as_dir(self)->Path:
        assert self.as_local_path.is_dir()
        return self.as_local_path



    def read(self, *, offset:int=0, length:int=None)->bytes:
        file_path=self.as_local_path
        with open(file_path, "rb") as file_buffer:
            if offset>0:
                file_buffer.seek(offset)
            if length is not None:
                if length > 0:
                    return file_buffer.read(length)
                return b''
            return file_buffer.read()
        