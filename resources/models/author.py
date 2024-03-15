from cloudevents.http import CloudEvent
from pydantic import BaseModel


class AuthorModel(BaseModel):
    _author_name: str
    _author_id: str
    _author_token: str

    @property
    def authorname(self):
        return self._author_name

    @authorname.setter
    def authorname(self, value: str) -> None:
        self._author_name = value

    @authorname.deleter
    def authorname(self) -> str:
        tmp = self._author_name
        self._author_name = None

        return tmp

    @property
    def authorid(self):
        return self._author_id

    @authorid.setter
    def authorid(self, value: str) -> None:
        self._author_id = value

    @authorid.deleter
    def authorid(self) -> str:
        tmp = self._author_id
        self._author_id = None

        return tmp

    @property
    def authortoken(self):
        return self._author_token

    @authortoken.setter
    def authortoken(self, value: str) -> None:
        self._author_token = value

    @authortoken.deleter
    def authortoken(self) -> str:
        Warning("Deleting the author token is not allowed")

    def marshal(self):
        # marshal the AuthorModel instance and return a dictionary containing
        # the AuthorModel instance's attributes
        # This is useful for creating a CloudEvent instance (see resources/event.py)
        #
        # Example: event = CloudEvent(**author.marshal())

        return {
            "author_name": self._author_name,
            "author_id": self._author_id,
            "author_token": self._author_token
        }

    @classmethod
    def unmarshal(cls, event: CloudEvent):
        # unmarsal the event and return an AuthorModel instance from the event's attributes
        # This is useful for deserializing a CloudEvent instance (see resources/event.py)
        #
        # Example:  event = CloudEvent(**author.marshal())
        #           author = AuthorModel.unmarshal(event)

        attributes = event.get_attributes()
        cls.authorid = attributes['authorid']
        cls.authorname = attributes['authorname']
        cls.authortoken = attributes['authortoken']

        return cls
