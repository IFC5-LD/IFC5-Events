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


    def marshal(self, format: str = "json") -> dict:
        """
        Marshal the DataModel instance into an agnostic format
        by returning a dictionary containing the DataModel instance's
        attributes

        :return: dict
        """

        ret = {
            "data_encoding": self.data_encoding,
            "data_encryption": self.data_encryption,
            "data_hash": self.data_hash
        }

        if format == "cloudevent":
            return {k.replace("_", ""): v for k, v in ret.items()}
        else:
            return ret

    @classmethod
    def unmarshal(cls, data: dict) :
        """
        Unmarshal the DataModel instance and return a dictionary containing
        :param event:
        :return:
        """
        print(hash(data.get("data")))

        return DataModel(
            data_encoding=data.get("data_encoding", "utf-8"),
            data_encryption=data.get("data_encryption", ""),
            data_hash=data.get("data_hash", hash(data.get("data"))),
            data=data.get("data")
        )

