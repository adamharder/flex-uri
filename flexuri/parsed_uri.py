

from dataclasses import dataclass
from typing import List
from pathlib import Path
import urllib # from urllib import parse

@dataclass
class ParsedUri(object):
    scheme:str
    parts:List
    path:Path
    netloc:str
    params:str
    query:str
    fragment:str


    @staticmethod
    def parse(uri_str:str):
        scheme=uri_str.split("://")[0]
        temp_uri="file"+uri_str[len(scheme):]

        print (temp_uri)
        parsed=urllib.parse.urlparse(temp_uri)
        print(parsed)
        return ParsedUri(scheme=scheme, path=Path(parsed.path), parts=Path(parsed.path).parts, netloc=parsed.netloc,params=parsed.params, query=parsed.query, fragment=parsed.fragment)
    def __str__(self):
        return f"{self.scheme}://{self.netloc}{self.path}"
    @property
    def as_json(self):
        return dict(
            scheme=self.scheme, path=str(self.path), parts=self.parts, 
            netloc=self.netloc,
            params=self.params, 
            query=self.query, fragment=self.fragment)
        

print(ParsedUri.parse("xyz://a/bcd"))