from typing import Union, BinaryIO

from cloudevents.abstract import CloudEvent
from pydantic import BaseModel

from resources.models.helpers.hash import hash

class DataModel(BaseModel):
    """
    The DataModel class is a Pydantic BaseModel that represents the data property of an event.
    The data property is a required property of an event.

    Properties:
    - data: Union[dict, BinaryIO]
        The data property is a Union of a dictionary or a BinaryIO object that represents
        the data being carried by the event. The data property is a required property.
    - dataencoding: str
        The dataencoding property is a string that represents the encoding of the data property.
    - dataencryption: str
        The dataencryption property is a string that represents the encryption of the data property.
    - datahash: str
        The datahash property is a string that represents the hash of the data property.

    """
    _data_encoding: str = "utf-8"
    _data_encryption: str = None
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
    def dataencoding(self, value: str=None) -> None:
        if value:
            self._data_encoding = value
        else:
            self._data_encoding = "utf-8"

    @dataencoding.deleter
    def dataencoding(self) -> str:
        """
        Delete the data encoding property and return the value of the data encoding property

        :return: str
        """
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
        Warning("Deleting the event encryption is not allowed")

    @property
    def datahash(self):
        return self._data_hash

    @datahash.setter
    def datahash(self, value: str, data: Union[str, dict]=None) -> None:
        """
        Set the data hash property. This method may be used by either passing a
        literal SHA256 hash or by passing the data object as a dict or string to be hashed.

        :param value:
        :param data:
        :return:
        """

        if data:
            self._data_hash = hash(data, self._data_encoding)
        else:
            self._data_hash = value

    @datahash.deleter
    def datahash(self) -> str:
        Warning("Deleting the event hash is not allowed")

    def marshal(self) -> dict:
        """
        Marshal the DataModel instance into an agnostic format
        by returning a dictionary containing the DataModel instance's
        attributes

        :return: dict
        """

        return {
            "dataencoding": self.dataencoding,
            "dataencryption": self.dataencryption,
            "datahash": self.datahash
        }

    @classmethod
    def unmarshal(cls, event: CloudEvent):
        """
        Unmarshal the DataModel instance and return a dictionary containing
        :param event:
        :return:
        """

        attributes = event.get_attributes()
        cls.dataencoding = attributes['dataencoding']
        cls.dataencryption = attributes['dataencryption']
        cls.datahash = hash(str(attributes['data']))
        cls.data = event.get_data()

