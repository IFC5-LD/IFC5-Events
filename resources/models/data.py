from typing import Union, BinaryIO
from pydantic import BaseModel

from hash import hash

class DataModel(BaseModel):
    _data_encoding: str
    _data_encryption: str
    _data_hash: str
    _data: Union[dict, BinaryIO]

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value: Union[dict, BinaryIO]) -> None:
        self._data = value

    @property
    def dataencoding(self):
        return self._data_encoding

    @dataencoding.setter
    def dataencoding(self, value: str) -> None:
        self._data_encoding = value

    @dataencoding.deleter
    def dataencoding(self) -> str:
        tmp = self._data_encoding
        self._data_encoding = None

        return tmp

    @property
    def dataencryption(self):
        return self._data_encryption

    @dataencryption.setter
    def dataencryption(self, value: str) -> None:
        self._data_encryption = value

    @dataencryption.deleter
    def dataencryption(self) -> str:
        Warning("Deleting the data encryption is not allowed")

    @property
    def datahash(self):
        return self._data_hash

    @datahash.setter
    def datahash(self, value: str, data: Union[str, dict]=None) -> None:
        if data:
            self._data_hash = hash(data)
        else:
            self._data_hash = value

    @datahash.deleter
    def datahash(self) -> str:
        Warning("Deleting the data hash is not allowed")

    def marshal(self) -> dict:
        return {
            "dataencoding": self.dataencoding,
            "dataencryption": self.dataencryption,
            "datahash": self.datahash
        }

    def unmarshal(self, data: dict) -> None:
        # TODO: Revisit the general logic here
        self._data_encoding = data['_data_encoding']
        self._data_encryption = data['_data_encryption']
        self._data_hash = data['_data_hash']
