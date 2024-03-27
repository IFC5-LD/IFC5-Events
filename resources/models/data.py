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
    data_encoding: str = "utf-8"
    data_encryption: str = None
    data_hash: str = None
    data: Union[dict] = None

    @property
    def dataencoding(self):
        return self.data_encoding

    @dataencoding.setter
    def dataencoding(self, value: str=None) -> None:
        if value:
            self.data_encoding = value
        else:
            self.data_encoding = "utf-8"

    @dataencoding.deleter
    def dataencoding(self) -> str:
        """
        Delete the data encoding property and return the value of the data encoding property

        :return: str
        """
        tmp = self.data_encoding
        self.data_encoding = None

        return tmp

    @property
    def dataencryption(self):
        return self.data_encryption

    @dataencryption.setter
    def dataencryption(self, value: str) -> None:
        self.data_encryption = value

    @dataencryption.deleter
    def dataencryption(self) -> str:
        Warning("Deleting the event encryption is not allowed")

    @property
    def datahash(self):
        return self.data_hash

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
            self.data_hash = hash(data, self.data_encoding)
        else:
            self.data_hash = value

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
    def unmarshal(cls, data: dict) :
        """
        Unmarshal the DataModel instance and return a dictionary containing
        :param event:
        :return:
        """

        return DataModel(
            data_encoding=data.get("dataencoding", "utf-8"),
            data_encryption=data.get("dataencryption", ""),
            data_hash=data.get("datahash", hash(data.get("data"))),
            data=data.get("data", {})
        )

