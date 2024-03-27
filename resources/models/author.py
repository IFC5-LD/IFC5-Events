from cloudevents.http import CloudEvent
from pydantic import BaseModel


class AuthorModel(BaseModel):
    author_name: str = ""
    author_id: str = ""
    author_token: str = ""

    @property
    def authorname(self):
        return self.author_name

    @authorname.setter
    def authorname(self, value: str) -> None:
        self.author_name = value

    @authorname.deleter
    def authorname(self) -> str:
        tmp = self.author_name
        self.author_name = None

        return tmp

    @property
    def authorid(self):
        return self.author_id

    @authorid.setter
    def authorid(self, value: str) -> None:
        self.author_id = value

    @authorid.deleter
    def authorid(self) -> str:
        tmp = self.author_id
        self.author_id = None

        return tmp

    @property
    def authortoken(self):
        return self.author_token

    @authortoken.setter
    def authortoken(self, value: str) -> None:
        self.author_token = value

    @authortoken.deleter
    def authortoken(self):
        Warning("Deleting the author token is not allowed")

    def marshal(self):
        # marshal the AuthorModel instance and return a dictionary containing
        # the AuthorModel instance's attributes
        # This is useful for creating a CloudEvent instance (see resources/event.py)
        #
        # Example: event = CloudEvent(**author.marshal())

        return {
            "authorname": self.authorname,
            "authorid": self.authorid,
            "authortoken": self.authortoken
        }

    @classmethod
    def unmarshal(cls, data: dict):
        # unmarsal the event and return an AuthorModel instance from the event's attributes
        # This is useful for deserializing a CloudEvent instance (see resources/event.py)
        #
        # Example:  event = CloudEvent(**author.marshal())
        #           author = AuthorModel.unmarshal(event)

        return AuthorModel(
            author_name=data['authorname'],
            author_id=data['authorid'],
            author_token=data['authortoken']
        )
