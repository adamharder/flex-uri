# any Flex URI implementation must inherit from FlexUriBase
from dataclasses import dataclass
from .parsed_uri import ParsedUri

@dataclass
class FlexUriBase():
    uri:ParsedUri

    @property
    def scheme(self):
        return self.uri.scheme
    @property
    def path(self):
        return self.uri.path
    def __str__(self):
        return str(self.uri)
    @property
    def suffix(self):
        return self.uri.path.suffix
    @property
    def stem(self):
        return self.uri.path.stem
    @property
    def as_json(self):
        return self.uri.as_json

    def get_blob(self, file_path, confirm=True):
        return self.get_file(file_path=file_path, confirm=confirm)