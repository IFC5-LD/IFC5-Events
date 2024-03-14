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
        return {
            "author_name": self._author_name,
            "author_id": self._author_id,
            "author_token": self._author_token
        }

    def unmarshal(self, data: dict):
        self._author_name = data['author_name']
        self._author_id = data['author_id']
        self._author_token = data['author_token']